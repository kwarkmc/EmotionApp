import matplotlib.pyplot as plt
import os
import numpy as np
import librosa
import librosa.display
import sklearn
from unicodedata import normalize

pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))

import warnings
warnings.filterwarnings('ignore')

DATA_DIR = './Datasets'

trainset = []
testset = []

train_X = []
train_mfccs = []
train_y = []

test_X = []
test_mfccs = []
test_y = []

frame_length = 0.025
frame_stride = 0.0010

filename = os.listdir(DATA_DIR)

#Train Data MFCC 적용

for filename in os.listdir(DATA_DIR + "train_real/"):
    filename = normalize('NFC', filename)
    try:
        if '.wav' not in filename in filename:
            continue
        wav, sr = librosa.load(DATA_DIR + "train_real/" + filename, sr=None)
        print(filename)
        
        mfcc = librosa.feature.mfcc(y=wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
        mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
        padded_mfcc = pad2d(mfcc, 700)
        
        np.save(DATA_DIR + 'train/' + filename[:-4], padded_mfcc)
    
    except Exception as e:
        print(filename, e)
        raise

for filename in os.listdir(DATA_DIR + "test_real/"):
    filename = normalize('NFC', filename)
    try:
        if '.wav' not in filename in filename:
            continue
        wav, sr = librosa.load(DATA_DIR + "test_real/" + filename, sr=None)
        print(filename)
        
        mfcc = librosa.feature.mfcc(y=wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
        mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
        padded_mfcc = pad2d(mfcc, 700)
        
        np.save(DATA_DIR + 'test/' + filename[:-4], padded_mfcc)
        
    except Exception as e:
        print(filename, e)
        raise