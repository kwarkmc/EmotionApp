import speech_recognition as sr
import os
from pydub import AudioSegment

path = r"C:\Users\User\Desktop\딥러닝\voice"
filePath=r"1. VoiceToEmotion_Data_Audio.wav"
os.chdir(path)
audio_files = os.listdir()
name, ext = os.path.splitext(filePath)
if ext == ".mp3":
     mp3_sound = AudioSegment.from_file(filePath)
     mp3_sound.export("{0}.wav".format(name), format="wav")



harvard_audio = sr.AudioFile(name+"wav")
with harvard_audio as source:
     audio = recognizer.record(source)

try:
     text = recognize.recognize_google(audio, language='ko-KR')
     print (text)
except Exception as e:
     print ()
