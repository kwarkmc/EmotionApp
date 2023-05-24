from keras.models import load_model
import numpy as np
import librosa
import sklearn
import os
from unicodedata import normalize
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import tensorflow as tf
from datetime import date
import speech_recognition as VTT

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def process_audio_files():

    today = date.today().strftime('%y%m%d')
    pad2d = lambda a, i: a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i-a.shape[1]))))
    
    VTE_Array = []
    TTE_Array = []
    
    CNN_model = load_model('weights/weight_result.h5')

    directory_audio = f"{today}/"
    directory_txt = f"{today}/TXT/"
    for filename in os.listdir(directory_audio): #TODO 오늘 날짜 폴더를 지정해서 파일 불러오는 방식으로 수정
        filename = normalize('NFC', filename)
        try:
            if '.wav' not in filename in filename:
                continue
            wav, sr = librosa.load(directory_audio + filename, sr=None)
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

    #Voice To Text Processing

    if not os.path.exists(directory_txt):
        os.makedirs(directory_txt)

    for filename in os.listdir(directory_audio):
        if not filename.endswith('.wav'):
            continue

        filename = normalize('NFC', filename)
        try:
            r = VTT.Recognizer()
            kr_audio = VTT.AudioFile(directory_audio + filename)
            with kr_audio as source:
                VTT_audio = r.record(source)

            temp = r.recognize_google(VTT_audio, language='ko-KR')

            # Get the file name without extension
            name = os.path.splitext(filename)[0]
            with open(directory_txt + str(name) + 'out.txt', 'w') as f:
                first_line = temp.split('\n')[0]
                print(first_line, file=f)

        except Exception as e:
            print(f"Error processing file {filename}: {str(e)}")

    rnn_model = tf.keras.models.load_model("weights/model_04", custom_objects={"TextVectorization": TextVectorization})

    for filename in os.listdir(directory_txt):
        filename = normalize('NFC', filename)
        try:
            if '.txt' not in filename in filename:
                continue
            f = open(directory_txt + filename, "r", encoding='euc-kr')
            input_txt = f.read().strip()
            f.close()

            emotion = float(rnn_model.predict([input_txt]))
            TTE_Array.append(emotion)

        except Exception as e:
            print(filename, e)
            raise

    # VTE_Array의 평균
    VTE_Array = np.array(VTE_Array)
    VTE_Mean = np.mean(VTE_Array, axis=0)
    VTE_Mean = (VTE_Mean[0][0] + VTE_Mean[0][1]) / 2
    TTE_Array = np.array(TTE_Array)
    TTE_Mean = np.mean(TTE_Array, axis=0)

    result = (VTE_Mean + TTE_Mean) / 2
    result = round(result, 4)
    result = result * 100

    return result

if __name__ == '__main__':
    result = process_audio_files()
    print(result)