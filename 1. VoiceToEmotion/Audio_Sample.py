from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from collections import defaultdict, Counter
from scipy import signal
import librosa
import sklearn
from VoiceToEmotion import pad2d


DATA_DIR = 'Data/Sample/'

wav, sr = librosa.load(DATA_DIR + 'Sample1.wav', sr=None)
print('sr : ', sr)
print('wav shape : ', wav.shape)
print('length : ', wav.shape[0]/float(sr), 'secs')

audio, sr = librosa.load(DATA_DIR + 'Sample1.wav', sr=None)
mfcc = librosa.feature.mfcc(y = wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
padded_mfcc = pad2d(mfcc, 40)
padded_mfcc = np.expand_dims(padded_mfcc, 0)


