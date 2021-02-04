import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You Said ",text)
    except:
        print("Sorry couldnt recognize ur voice")