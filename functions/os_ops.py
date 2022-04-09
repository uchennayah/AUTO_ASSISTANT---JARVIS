import os
import subprocess as sp

paths = {
    "music" : "/System/Applications/Music.app" ,
    "calculator" : "/System/Applications/Calculator.app" ,
    "books": "/System/Applications/Books.app",
    "calendar": "/System/Applications/Calendar.app"
}


# Opening the camera
def open_camera():
    sp.run('start mac.wwindows.camera:', shell = True)


def open_music():
    os.startfile(paths['music'])

def open_calculator():
    sp.Popen(paths['calculator'])  

def books():
    os.startfile(paths['books'])      

def open_calendar():
    os.startfile(paths['calendar'])


def open_terminal():
    os.system('start cmd')