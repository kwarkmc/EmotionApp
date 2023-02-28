import speech_recognition as sr
import os
import sys


path = '경로'
file_list = os.listdir(path)
file_list_wav = [file for file in file_list if file.endswith('.wav')]

name = 0
for i in file_list_wav:
    
    r = sr.Recognizer()
    kr_audio = sr.AudioFile(path + "\" + i)

    with kr_audio as source:
        audio = r.record(source)

    temp = r.recognize_google(audio, language='ko-KR')

    sys.stdout = open(name+'out.txt', 'w')
    print(temp)
    sys.stdout.close()
   
    name = name+1
