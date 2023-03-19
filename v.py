import requests
from vosk import Model,KaldiRecognizer
import pyaudio
import pyttsx3

model=Model(r'vosk-model-en-in-0.5')
recognizer=KaldiRecognizer(model,16000)
mic=pyaudio.PyAudio()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',140)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    stream=mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
    stream.start_stream()
    print('listening....')
    while True:
        data=stream.read(4096,exception_on_overflow = False)
        if len(data)==0:
            return ''
        if recognizer.AcceptWaveform(data):
            text=recognizer.Result()
            print(text[14:-3])
            return text[14:-3]

msg=''
count=0
speak("Hey my name is Luna. How can I help you?")
while True:
    msg = takeCommand().lower()
    if('luna' in msg):
        if(msg=='luna' or msg.endswith('luna')):
            continue
        msg=msg.split("luna",1)[1]
        print(msg)
        r=requests.post('http://localhost:5002/webhooks/rest/webhook',json={"message":msg})
        print('Bot says, ',end=' ')
        for i in r.json():
            res=i['text']
            if res=='I am unable to understand, can you please reframe the sentence':
                if(count==1):
                    speak('Kindly contact Professor Karthik for more queries. His email ID is admissions@cambridge.edu.in')
                    count=0
                    continue
                count+=1
            else:
                count=0
            speak(res)

