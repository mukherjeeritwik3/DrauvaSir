import pyttsx3
import speech_recognition as sr
import datetime
import time


# Initializing required pyttsx3 Properties
def text_Speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


# Setuping dateand Time

class dateTime:
    def __init__(self):
        self.d = datetime.datetime.today()

    # Creating Months finder property
    def months(self):
        monthS = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: ' August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        return monthS[self.d.month]

    # Creating Weekdays Name finder property
    def weekDays(self):
        weekdays = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'

        }
        return weekdays[self.d.weekday()]

    # Creating current date Property
    def currentDate(self):
        return self.d.day

    # Creating Current YEar Property
    def currentYear(self):
        return self.d.year

    # Current Time property
    def currentTime(self):
        return self.d.strftime("%I %M %p")


# Main function code for basic time related tasks
def dateTimeAssist(listner):
    timeNow = dateTime()
    a = {

        # Months related questions goes here
        'what month it is': "It is" + str(timeNow.months()),
        'what month is it': "It is" + str(timeNow.months()),
        'which month it is': "It is" + str(timeNow.months()),
        'which month is it': "It is" + str(timeNow.months()),
        'month now': "It is" + str(timeNow.months()),
        'current month': "It is" + str(timeNow.months()),
        'can you tell me the current month': "It is" + str(timeNow.months()),
        'can you tell me the month': "It is" + str(timeNow.months()),
        'can you tell me current month': "It is" + str(timeNow.months()),

        # Days or weekdays related question goes here
        'what day is it': "Today is" + str(timeNow.weekDays()),
        'what day is today': "Today is" + str(timeNow.weekDays()),
        'which day is it': "Today is" + str(timeNow.weekDays()),
        'which day is today': "Today is" + str(timeNow.weekDays()),

        # Full date year and month questions
        'tell me the current date': "Today is" + str(timeNow.currentDate()) + str(timeNow.months()) + str(
            timeNow.currentYear()),
        "what is today's date": "Today is" + str(timeNow.currentDate()) + str(timeNow.months()) + str(
            timeNow.currentYear()),
        'tell me the full date': "Today is" + str(timeNow.currentDate()) + str(timeNow.months()) + str(
            timeNow.currentYear()),

        # Year related questions
        'current year': "It is" + str(timeNow.currentYear()),
        'what year is it': "It is" + str(timeNow.currentYear()),
        'year now': "It is" + str(timeNow.currentYear()),
        'which year is it': "It is" + str(timeNow.currentYear()),
        'which year it is': "It is" + str(timeNow.currentYear()),
        'tell me the current year': "It is" + str(timeNow.currentYear()),

        # Time related question

        'tell me what time it is': "Currently it is" + str(timeNow.currentTime()),
        'what time it is': "Currently it is" + str(timeNow.currentTime()),
        'current time': "Currently it is" + str(timeNow.currentTime()),
        'time now': "Currently it is" + str(timeNow.currentTime()),
        "what's the time": "Currently it is" + str(timeNow.currentTime()),
        "time's now": "Currently it is" + str(timeNow.currentTime()),
        'tell me the current time': "Currently it is" + str(timeNow.currentTime()),

    }

    if (listner in a):
        return a[listner]
    else:
        return 0


# Setting Listen function for voice recognition
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
        time.sleep(0.5)
        text = listen()
        if text == "Sorry couldnt recognize ur voice":
            print(text)
            # text_Speech(text)   For debugging purpose
            continue
        else:
            # text_Speech(text)   For debugging Purpose
            if text == "computer":
                print(text)
                text_Speech("How may i be service to you sir?")

                text = listen()
                whistler = dateTimeAssist(text)
                if whistler == 0:
                    print("invalid")
                else:
                    text_Speech(whistler)
                continue
