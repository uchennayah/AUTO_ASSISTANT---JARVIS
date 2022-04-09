import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config 

EMAIL = config("EMAIL")
PASSWORD = config ('PASSWORD')

# search wikipedia
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 10)
    return results

# play youtube videos
def play_youtube(video):
    kit.playonyt(video)    

# search on google
def google_search(query):
    kit.search(query)

# send whatsapp messages
def send_whatsapp_messages (number, message):
    kit.sendwhatmsg_instantly(f"+234 {number}", message)

# send emails
def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()    
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_email(email)
        s.close()
        return True
    except Exception as e:
        print (e) 
        return False