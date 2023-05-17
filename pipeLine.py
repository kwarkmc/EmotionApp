from keras.models import load_model
import numpy as np
import librosa
import sklearn
import os
from unicodedata import normalize
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import tensorflow as tf

def process_audio_files():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))
    
    VTE_Array = []
    
    CNN_model = load_model('weights/weight_result.h5')

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

            VTE_result = CNN_model.predict(padded_mfcc)
            VTE_Array.append(VTE_result)

        except Exception as e:
            print(filename, e)
            raise

    if not os.path.exists('TXT'):
        os.makedirs('TXT')

    rnn_model = tf.keras.models.load_model("weights/model_04", custom_objects={"TextVectorization": TextVectorization})

    for filename in os.listdir("TXT/"):
        filename = normalize('NFC', filename)
        try:
            if '.txt' not in filename in filename:
                continue
            f = open('TXT/' + filename)
            input_txt = f.read().strip()
            f.close()

            emotion = float(rnn_model.predict([input_txt]))
            TTE_Array.append(emotion)

        except Exception as e:
            print(filename, e)
            raise

    # VTE_Array의 평균
    VTE_Array = np.array(VTE_Array)
    VTE_Array = np.mean(VTE_Array, axis=0)
    return VTE_Array

VTE_Array = process_audio_files()
print(VTE_Array)
