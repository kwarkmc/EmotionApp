import speech_recognition as sr
#import sys
import json

r = sr.Recognizer()
with sr.Microphone() as source:
    print("말하기")
    speech = r.listen(source)

data = {}

file_path = "sample.json"
#sys.stdout = open('audio_output.txt', 'w') #텍스트로 저장

try:
    with open(file_path, 'w',encoding='utf-8-sig') as out:
     audio = r.recognize_google(speech, language="ko-KR")
     data['message'] = audio
     print(audio)
     json.dump(data, out,ensure_ascii=False)
except sr.UnknownValueError:
    print("다시시도")
