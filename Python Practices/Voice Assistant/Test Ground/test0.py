import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You Said ",text)
        engine.say(text)
        engine.runAndWait()

    except:
        print("Sorry couldnt recognize ur voice")