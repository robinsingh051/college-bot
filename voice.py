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
    print('listening....')
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            statement = recognizer.recognize_google(audio, language='en-in')
            print(f"user said : {statement}\n")
        except Exception as e:
            print("Pardon me, can you please repeat?")
            return ""
        return statement

msg=''
speak("powering on. say hello to start conversation, and bye to end")
while True:
    msg = takeCommand().lower()
    if(msg=='hello'):
        speak("How can I help you?")
        while msg!='bye':
            msg = takeCommand().lower()
            if msg!='':
                r=requests.post('http://localhost:5002/webhooks/rest/webhook',json={"message":msg})
                print('Bot says, ',end=' ')
                for i in r.json():
                    res=i['text']
                    speak(res)