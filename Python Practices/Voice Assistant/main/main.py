import pyttsx3
import speech_recognition as sr
# Initializing required pyttsx3 Properties
def text_Speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

# Setuping Listen function for voice recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return ("Sorry couldnt recognize ur voice")


# Main codes goes here
if __name__ == '__main__':
    while True:
        text =listen()
        if (text == "Sorry couldnt recognize ur voice"):
            print(text)
           # text_Speech(text)   For debugging purpose
            continue
        else:
           # text_Speech(text)   For debugging Purpose
            print(text)
            break

