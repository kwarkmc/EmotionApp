import speech_recognition as sr
import os
import sys


path = r'C:\Users\User\Desktop\딥러닝\voice'
file_list = os.listdir(path)
file_list_wav = [file for file in file_list if file.endswith('.wav')]

name = 0
for i in file_list_wav:
    
    r = sr.Recognizer()
    kr_audio = sr.AudioFile(path+"/"+i)

    with kr_audio as source:
        audio = r.record(source)

    temp = r.recognize_google(audio, language='ko-KR')

    sys.stdout = open(str(name)+'out.txt', 'w')

    print(temp)

   
    name = name+1
