import requests
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',140)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        audio = recognizer.listen(source)
        
        try:
            statement = recognizer.recognize_google(audio, language='en-in')
            print(f"user said : {statement}\n")
        except Exception as e:
            speak("Pardon me, can you please repeat?")
            return "None"
        return statement

msg=''
while True:
    msg = takeCommand().lower()
    if(msg=='hello'):
        speak("How can I help you?")
        while msg!='bye':
            msg = takeCommand().lower()
            r=requests.post('http://localhost:5002/webhooks/rest/webhook',json={"message":msg})
            print('Bot says, ',end=' ')
            for i in r.json():
                res=i['text']
                speak(res)