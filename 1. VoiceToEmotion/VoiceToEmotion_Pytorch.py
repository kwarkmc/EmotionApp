import matplotlib.pyplot as plt
import os
import random
from scipy.io import wavfile
from collections import defaultdict, Counter
from scipy import signal
import numpy as np
import librosa
import librosa.display
import sklearn
from unicodedata import normalize
from sklearn import preprocessing
from keras.utils import to_categorical
import torch
import torch.nn as nn



import warnings

warnings.filterwarnings('ignore')

DATA_DIR = 'Data/'


trainset = []
testset = []


train_X = []
train_mfccs = []
train_y = []

test_X = []
test_mfccs = []
test_y = []


pad1d = lambda a, i: a[0:i] if a.shape[0] > i else np.hstack((a, np.zeros(i - a.shape[0])))
pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i - a.shape[1]))))

frame_length = 0.025
frame_stride = 0.0010

filename = os.listdir(DATA_DIR)

for filename in os.listdir(DATA_DIR + "train/"):
    filename = normalize('NFC', filename)
    try:

        if '.wav' not in filename in filename:
            continue

        wav, sr = librosa.load(DATA_DIR + "train/" + filename, sr=None)
        print(filename)

        mfcc = librosa.feature.mfcc(y=wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
        mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
        padded_mfcc = pad2d(mfcc, 700)


        if filename[0] == '긍':
            trainset.append((padded_mfcc, 0))
        elif filename[0] == '부':
            trainset.append((padded_mfcc, 1))
    except Exception as e:
        print(filename, e)
        raise


random.shuffle(trainset)


for filename in os.listdir(DATA_DIR + "test/"):
    filename = normalize('NFC', filename)
    try:

        if '.wav' not in filename in filename:
            continue

        wav, sr = librosa.load(DATA_DIR + "test/" + filename, sr=None)
        print(filename)

        mfcc = librosa.feature.mfcc(y=wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
        mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
        padded_mfcc = pad2d(mfcc, 700)


        if filename[0] == '긍':
            testset.append((padded_mfcc, 0))
        elif filename[0] == '부':
            testset.append((padded_mfcc, 1))
    except Exception as e:
        print(filename, e)
        raise


random.shuffle(testset)

train_mfccs = [a for (a, b) in trainset]
train_y = [b for (a, b) in trainset]

test_mfccs = [a for (a, b) in testset]
test_y = [b for (a, b) in testset]

train_mfccs = np.array(train_mfccs)
train_y = to_categorical(np.array(train_y))

test_mfccs = np.array(test_mfccs)
test_y = to_categorical(np.array(test_y))

print('train_mfccs:', train_mfccs.shape)
print('train_y:', train_y.shape)

print('test_mfccs:', test_mfccs.shape)
print('test_y:', test_y.shape)


train_X_ex = np.expand_dims(train_mfccs, -1)
test_X_ex = np.expand_dims(test_mfccs, -1)
print('train X shape:', train_X_ex.shape)
print('test X shape:', test_X_ex.shape)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=0)
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.fc1 = nn.Linear(in_features=32*49, out_features=64)
        self.fc2 = nn.Linear(in_features=64, out_features=2)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool1(x)
        x = x.view(-1, 32*49)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

model = Net()
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

train_X_ex = torch.tensor(train_X_ex, dtype=torch.float32)
train_y = torch.tensor(train_y, dtype=torch.float32)
test_X_ex = torch.tensor(test_X_ex, dtype=torch.float32)
test_y = torch.tensor(test_y, dtype=torch.float32)

for epoch in range(10):
    running_loss = 0.0
    for i in range(0, len(train_X_ex), 16):
        inputs = train_X_ex[i:i+16]
        labels = train_y[i:i+16]
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print('Epoch %d loss: %.3f' % (epoch + 1, running_loss / len(train_X_ex)))

torch.save(model.state_dict(), './weight.pt')
