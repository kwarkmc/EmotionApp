import speech_recognition as sr
#import sys

r = sr.Recognizer()
kr_audio = sr.AudioFile('C:/Users/User/Desktop/딥러닝/voice/1. VoiceToEmotion_Data_Audio_긍3.wav')

with kr_audio as source:
    audio = r.record(source)

temp = r.recognize_google(audio, language='ko-KR')

#sys.stdout = open('news_out.txt', 'w')
print(temp)

#sys.stdout.close()
