import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

# create a speech engine and initialize
USERNAME = config( "USER")
BOTNAME = config ("BOTNAME")

# Initia;ize a speech engine
engine = pyttsx3.init( "sapi5")

# set Rate
engine.setProperty('rate', 200)

# Set Volume
engine.setPropoerty ('volume', 1.5)

# Select a voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices [1].id)

 #Text to speech conversion
def speak (text):
     """ Repeats whatever text is passed to it"""
     engine.say(text)
     engine.runandWait()

 # Greet Function
def greet_user():
    """ Greets the user according to the time"""
    hour = datetime.now().hour    
    if (hour >= 6) and (hour < 12):
        speak (f"Good Morning{ USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak (f"Good Evening {USERNAME}")
    speak (f"I am {BOTNAME} built by {USERNAME}. How may I assist you?")    

# Collecting user input
def take_user_input():
    """ Accept user input and recognize it using Speech Recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Paying Attention...')
        r.puase_threshold = 3
        audio = r.listen(source)   

    try:
        print ("Recognizing user input.....")
        query = r.recognize_google(audio, language = 'en-uk')
        if not 'exit' in query or 'stop' in query:
            speak (choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak (f"Goodnight {USERNAME} sweet dreams")
            else:
                speak (f" Have a great day {USERNAME}")
            exit()
    except Exception:
        speak( 'Sorry, I dont understand what you are saying, can you please repeat it?')
        query = 'None'
    return query         