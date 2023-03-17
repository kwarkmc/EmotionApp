#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
from keras.models import load_model

import numpy as np
import librosa
import librosa.display
import sklearn
import matplotlib.pyplot as plt
import speech_recognition as VTT
import os
import sys


# In[2]:


DATA_DIR = 'Data/Sample'


# In[3]:


pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))


# In[4]:


#Audio = 원본 통화녹음 파일 Data/Sample/Sample1.wav

audio, sr = librosa.load(DATA_DIR + '/Sample1.wav', sr=None)
print('sr : ', sr)
print('wav shape : ', audio.shape)
print('length : ', audio.shape[0]/float(sr), 'secs')


# In[5]:


mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
padded_mfcc = pad2d(mfcc, 700)


# In[6]:


padded_mfcc = np.expand_dims(padded_mfcc, 0)


# In[7]:


padded_mfcc


# In[8]:


model = load_model('weight.h5')
VTE_result = model.predict(padded_mfcc)


# In[9]:


VTE_result


# In[10]:


r = VTT.Recognizer()
kr_audio = VTT.AudioFile('Data/Sample/Sample1.wav')


# In[11]:


name = 0


# In[12]:


with kr_audio as source:
    VTT_audio = r.record(source)


# In[13]:


temp = r.recognize_google(VTT_audio, language='ko-KR')


# In[ ]:


sys.stdout = open(str(name) + '.txt', 'w')
print(temp)
sys.stdout.close()


# In[ ]:


name = name + 1


# In[ ]:




