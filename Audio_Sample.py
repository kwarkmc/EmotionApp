#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from tensorflow.keras import models
#from tensorflow.keras import layers
#from tensorflow.keras import optimizers
#from tensorflow.keras import losses
#from tensorflow.keras import metrics
from keras.models import load_model

import numpy as np
import librosa
import librosa.display
import sklearn
import matplotlib.pyplot as plt
import speech_recognition as VTT
from unicodedata import normalize
import os
import sys


# In[2]:


pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))


# Voice To Emotion _ 곽민창

# In[3]:


VTE_Array = []
TTE_Array = []


# In[4]:


model = load_model('weight.h5')


# In[5]:


for filename in os.listdir("WAV/"):
    filename = normalize('NFC', filename)
    try:
        if '.wav' not in filename in filename:
            continue
        wav, sr = librosa.load("WAV/" + filename, sr=None)
        print(filename)
        
        mfcc = librosa.feature.mfcc(y=wav, sr=sr, n_mfcc=100, n_fft=400, hop_length=160)
        mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
        padded_mfcc = pad2d(mfcc, 700)
        padded_mfcc = np.expand_dims(padded_mfcc, 0)
        
        VTE_result = model.predict(padded_mfcc)
        VTE_Array.append(VTE_result)
        
    except Exception as e:
        print(filename, e)
        raise


# Voice To Text _ 이승렬

# In[7]:
if not os.path.exists('TXT'):
    os.makedirs('TXT')

for filename in os.listdir("WAV/"):
    if not filename.endswith('.wav'):
        continue
    
    filename = normalize('NFC', filename)
    try:
        r = VTT.Recognizer()
        kr_audio = VTT.AudioFile("WAV/" + filename)
        with kr_audio as source:
            VTT_audio = r.record(source)
            
        temp = r.recognize_google(VTT_audio, language='ko-KR')
        
        # Get the file name without extension
        name = os.path.splitext(filename)[0]
        with open("TXT/" + str(name) + 'out.txt', 'w') as f:
            first_line = temp.split('\n')[0]
            print(first_line, file=f)
    except Exception as e:
        print(f"Error processing file {filename}: {str(e)}")

        # TXT 파일을 name 변수에 따라 저장하는것이 아닌, 원본 wav 파일의 이름 뒤에 out.txt를 붙여서 저장하도록 수정


# Text To Emotion _ 김지호

# In[8]:


import nltk
from konlpy.tag import Okt
import json
okt = Okt()


# In[9]:


def read_data(filename):
    with open(filename, 'r', encoding = 'UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data


# In[10]:


def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]


# In[11]:


train_data = read_data("2. kimjiho/문자열_train_data.txt")
test_data = read_data("2. kimjiho/문자열_test_data.txt")


# In[12]:


if os.path.isfile('2. kimjiho/train_docs.json'):
    with open('2. kimjiho/train_docs.json',encoding="UTF-8")as f:
        train_docs = json.load(f)
    with open('2. kimjiho/test_docs.json',encoding="UTF-8")as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[0]),row[1]) for row in train_data]
    test_docs = [(tokenize(row[0]),row[1]) for row in test_data]
    with open('2. kimjiho/train_docs.json','w',encoding="UTF-8")as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('2. kimjiho/test_docs.json','w',encoding="UTF-8")as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")


# In[13]:


tokens = [t for d in train_docs for t in d[0]]
text = nltk.Text(tokens, name='NMSC')
selected_words = [f[0] for f in text.vocab().most_common(20000)]
def term_frequency(doc):
    return [doc.count(word) for word in selected_words]


# In[14]:


#감정 추출해주는 Result 함수
def predict_pos_neg(review):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.array(tf).astype('float32'),axis=0)
    score = float(model.predict(data))
    if(score>0.5):
        print("오늘의 긍정지수는 {:2f}%입니다.\n".format(score*100))
        return score*100
    else:
        print("오늘의 부정지수는 {:2f}%입니다.\n".format((1-score)*100))
        return score*100


# In[16]:


for filename in os.listdir("TXT/"):
    filename = normalize('NFC', filename)
    try:
        if '.txt' not in filename in filename:
            continue
        f = open('TXT/' + filename)
        input_txt = f.read()
        f.close()
        print(input_txt)

        TTE_Result = predict_pos_neg("오늘은 기분이 안좋아")
        #TTE_Result = predict_pos_neg(input_txt)
        TTE_Array.append(TTE_Result)
        
    except Exception as e:
        print(filename, e)
        raise
        
    #TODO : _지호 입력 데이터의 형태(shape)나 타입(type)이 모델과 맞지 않는 경우, 모델의 파라미터나 하이퍼파라미터가 잘못 설정된 경우, 모델의 레이어나 옵티마이저가 호환되지 않는 경우
    #오류 발생,,,

