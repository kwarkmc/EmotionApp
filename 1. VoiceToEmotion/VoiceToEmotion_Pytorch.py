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
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader



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

class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y).float()

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(100, 32, kernel_size=3)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(32 * 49 * 231, 6)
        self.relu2 = nn.ReLU()
        self.fc2 = nn.Linear(64, 2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu2()
        x = self.fc2()
        x = self.sigmoid(x)
        return x

num_epoch = 10
batch_size = 16
learning_rate = 0.001

train_dataset = MyDataset(train_X_ex, train_y)
test_dataset = MyDataset(test_X_ex, test_y)

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)


model = MyModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr = learning_rate)

for epoch in range(num_epoch):
    for X, y in train_dataloader:
        y_pred = model(X)
        loss = criterion(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        correct = 0
        total = 0
        for X, y in test_dataloader:
            y_pred = model(X)
            predicted = torch.round(y_pred)
            total += y.size(0)
            correct += (predicted == y).sum().item()
        accuracy = 100 * correct / total

    print(f"Epoch [{epoch + 1}/{num_epoch}], Loss : {loss.item():.4f}, Accuracy : {accuracy:.2f}%")

torch.save(model.state_dict(), './weight.pt')
