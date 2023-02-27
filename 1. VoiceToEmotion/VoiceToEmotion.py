#!/usr/bin/env python
# coding: utf-8

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
import tensorflow as tf
from keras import layers
import random as rn
from keras.layers import Dense
from keras import Input
from keras import Model
from keras.utils import to_categorical


# In[2]:


import warnings
warnings.filterwarnings('ignore')

DATA_DIR = 'Data/'

#데이터셋 리스트, raw data, mfcc data, y data를 포함한다.
trainset = []
testset = []

#STFT 한 것, CNN 분석하기 위해 Spectogram으로 만든것, MF 한 것, mel0spectogram 한 것
train_X = []
train_mfccs = []
train_y = []

test_X = []
test_mfccs = []
test_y = []

#모든 음성파일의 길이가 같도록 뒤에 padding 처리 한다.
pad1d = lambda a, i: a[0:i] if a.shape[0] > i else np.hstack((a, np.zeros(i-a.shape[0])))
pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))

frame_length = 0.025
frame_stride = 0.0010

filename = os.listdir(DATA_DIR)

#wav, sr = librosa.load(DATA_DIR + 'train/' + '부100.wav', sr=None)
#Sampling Rate 는 48000로 고정

#mfcc = librosa.feature.mfcc(y = wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
#mfcc 매서드를 사용하여 mfcc 변환 진행
#파라메터 설명 필요!

#mfcc = sklearn.preprocessing.scale(mfcc, axis=1)

#padded_mfcc = pad2d(mfcc, 700)
#40 = 0.46s
#pad2d parameter 값으로 padding을 진행할 수 있다. 음성 데이터의 평균 길이로 선택할 것.

#librosa.display.specshow(padded_mfcc)
#mfcc 한 데이터를 시각화 하여 볼 수 있음

# train data를 넣는다.
for filename in os.listdir(DATA_DIR + "train/"):
  filename = normalize('NFC', filename)
  try:
    # wav 포맷 데이터만 사용
    if '.wav' not in filename in filename:
      continue
      
    wav, sr = librosa.load(DATA_DIR+ "train/"+ filename, sr=None)
    print(filename)
    
    mfcc = librosa.feature.mfcc(y = wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    padded_mfcc = pad2d(mfcc, 700)

    # 긍정/부정 데이터 Labeling
    if filename[0] == '긍':
      trainset.append((padded_mfcc, 0))
    elif filename[0] == '부':
      trainset.append((padded_mfcc, 1))
  except Exception as e:
    print(filename, e)
    raise

# 학습 데이터를 무작위로 섞는다.
random.shuffle(trainset)


# test data를 넣는다.
for filename in os.listdir(DATA_DIR + "test/"):
  filename = normalize('NFC', filename)
  try:
    # wav 포맷 데이터만 사용
    if '.wav' not in filename in filename:
      continue

    wav, sr = librosa.load(DATA_DIR + "test/" + filename, sr=None)
    print(filename)

    mfcc = librosa.feature.mfcc(wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    padded_mfcc = pad2d(mfcc, 700)

    # 긍정/부정 데이터 Labeling
    if filename[0] == '긍':
      testset.append((padded_mfcc, 0))
    elif filename[0] == '부':
      testset.append((padded_mfcc, 1))
  except Exception as e:
    print(filename, e)
    raise

# 평가 데이터를 무작위로 섞는다.
random.shuffle(testset)

train_mfccs = [a for (a,b) in trainset]
train_y = [b for (a,b) in trainset]

test_mfccs = [a for (a,b) in testset]
test_y = [b for (a,b) in testset]

train_mfccs = np.array(train_mfccs)
train_y = to_categorical(np.array(train_y))

test_mfccs = np.array(test_mfccs)
test_y = to_categorical(np.array(test_y))

print('train_mfccs:', train_mfccs.shape)
print('train_y:', train_y.shape)

print('test_mfccs:', test_mfccs.shape)
print('test_y:', test_y.shape)


""" 데이터셋 구성 완료"""

train_X_ex = np.expand_dims(train_mfccs, -1)
test_X_ex = np.expand_dims(test_mfccs, -1)
print('train X shape:', train_X_ex.shape)
print('test X shape:', test_X_ex.shape)

"""
ip = Input(shape=train_X_ex[0].shape)

m = Conv2D(32, kernel_size=(4,4), activation='relu')(ip)
m = MaxPooling2D(pool_size=(4,4))(m)

m = Conv2D(32*2, kernel_size=(4,4), activation='relu')(ip)
m = MaxPooling2D(pool_size=(4,4))(m)

m = Conv2D(32*3, kernel_size=(4,4), activation='relu')(ip)
m = MaxPooling2D(pool_size=(4,4))(m)

m = Flatten()(m)

m = Dense(64, activation='relu')(m)

m = Dense(32, activation='relu')(m)

op = Dense(3, activation='softmax')(m)

model = Model(ip, op)

model.summary()


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(train_X_ex,
                    train_y,
                    epochs=100,
                    batch_size=32,
                    verbose=1,
                    validation_data=(test_X_ex, test_y))
"""

model = tf.keras.Sequential()
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(100, 700, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_X_ex, train_y, epochs=10, batch_size=16, validation_data=(test_X_ex, test_y))

model.save('./weight.h5')

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
