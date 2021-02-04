import pyttsx3
engine = pyttsx3.init()
# Setting voices as voice list variable
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#Setting speed or rate of voice
engine.setProperty('rate',200)
engine.say("10:30 PM")
engine.runAndWait()