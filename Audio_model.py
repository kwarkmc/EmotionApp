#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import random
import numpy as np
import librosa
import librosa.display
import sklearn
from unicodedata import normalize
import tensorflow as tf
from keras import layers
from keras.utils import to_categorical


# In[2]:


DATA_DIR = '1. VoiceToEmotion/Data/'


# In[3]:


trainset = []
testset = []


# In[4]:


train_X = []
train_mfccs = []
train_y = []


# In[5]:


test_X = []
test_mfccs = []
test_y = []


# In[6]:


frame_length = 0.025
frame_stride = 0.0010


# In[7]:


filename = os.listdir(DATA_DIR)


# In[8]:


for filename in os.listdir(DATA_DIR + "train/"):
    filename = normalize('NFC', filename)
    try:
        if '.npy' not in filename in filename:
            continue
            
        padded_mfcc = np.load(DATA_DIR + 'train/' + filename, allow_pickle=True)
        print(filename)
        
        if filename[0] == '긍':
            trainset.append((padded_mfcc, 0))
        elif filename[0] == '부':
            trainset.append((padded_mfcc, 1))
    except Exception as e:
        print(filename, e)
        raise

random.shuffle(trainset)


# In[10]:


for filename in os.listdir(DATA_DIR + "test/"):
    filename = normalize('NFC', filename)
    try:
        if '.npy' not in filename in filename:
            continue
            
        padded_mfcc = np.load(DATA_DIR + 'test/' + filename, allow_pickle=True)
        print(filename)
        
        if filename[0] == '긍':
            testset.append((padded_mfcc, 0))
        elif filename[0] == '부':
            testset.append((padded_mfcc, 1))
    except Exception as e:
        print(filename, e)
        raise

random.shuffle(testset)


# In[11]:


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


# In[12]:


train_X_ex = np.expand_dims(train_mfccs, -1)
test_X_ex = np.expand_dims(test_mfccs, -1)

print('train X shape:', train_X_ex.shape)
print('test Y shape:', test_X_ex.shape)


# In[13]:


model = tf.keras.Sequential()
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(100, 700, 1)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[14]:


history = model.fit(train_X_ex, train_y, epochs=10, batch_size=16, validation_data=(test_X_ex, test_y))


# In[ ]:


model.save("weight.h5")

