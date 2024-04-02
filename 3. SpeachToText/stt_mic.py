import speech_recognition as sr
#import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    print("말하기")
    speech = r.listen(source)

#sys.stdout = open('audio_output.txt', 'w') #텍스트로 저장

try:
    audio = r.recognize_google(speech, language="ko-KR")
    print(audio)
except sr.UnknownValueError:
    print("다시시도")
