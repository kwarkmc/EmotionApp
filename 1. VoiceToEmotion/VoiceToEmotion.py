#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from collections import defaultdict, Counter
from scipy import signal
import numpy as np
import librosa
import librosa.display
import sklearn
from unicodedata import normalize
import random as rn
from keras.layers import Dense
from keras import Input
#from tensorflow.python.keras.engine import Model
from keras.utils import to_categorical
#from tensorflow.keras.layers import Dense, TimeDistributed, Dropout, Bidirectional, GRU, BatchNormalization, Activation, LeakyReLU, LSTM, Flatten, RepeatVector, Permute, Multiply, C


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


DATA_DIR = 'Data/'


# In[7]:


wav, sr = librosa.load(DATA_DIR + 'train/' + '긍100.wav', sr=None)
print('sr : ', sr)
print('wav shape : ', wav.shape)
print('length : ', wav.shape[0]/float(sr), 'secs')


# In[8]:


print(plt.plot(wav))


# In[9]:


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


# In[10]:


filename = os.listdir(DATA_DIR)


# In[12]:


wav, sr = librosa.load(DATA_DIR + 'train/' + '부100.wav', sr=None)
#Sampling Rate 는 48000로 고정


# In[13]:


mfcc = librosa.feature.mfcc(y = wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
#mfcc 매서드를 사용하여 mfcc 변환 진행
#파라메터 설명 필요!


# ![image.png](attachment:image.png)

# In[14]:


mfcc = sklearn.preprocessing.scale(mfcc, axis=1)


# In[80]:


padded_mfcc = pad2d(mfcc, 700)
padded_mfcc.shape
#40 = 0.46s
#pad2d parameter 값으로 padding을 진행할 수 있다. 음성 데이터의 평균 길이로 선택할 것.


# In[81]:


librosa.display.specshow(padded_mfcc)
#mfcc 한 데이터를 시각화 하여 볼 수 있음


# In[ ]:


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

    # 추임새 별로 dataset에 추가
    if filename[0] == '긍':
      trainset.append((padded_mfcc, 0))
    elif filename[0] == '부':
      trainset.append((padded_mfcc, 1))
  except Exception as e:
    print(filename, e)
    raise

# 학습 데이터를 무작위로 섞는다.
random.shuffle(trainset)


# In[ ]:




