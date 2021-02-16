import os
import time

from tkinter import EXCEPTION

import pyttsx3
import PyPDF2
from tkinter.filedialog import *
import speech_recognition as sr


listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#
# book= askopenfilename()
# pdfreader=PyPDF2.PdfFileReader(book)
# pages=pdfreader.numPages

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = ''
            try:
                print("Recognizing...")
                command = listener.recognize_google(voice, language='en-in')
                command = command.lower()
                if 'jerry' in command:
                    command = command.replace('romeo', '')
                    print(command)
                else:
                    pass
                # return command
            except:
                pass
                speak('Unable to Recognize your voice.')
            return command

    except Exception as e:
        print(e)
        speak('No internet service avaiable')


def speak(text):
    engine.say(text)
    engine.runAndWait()



def run_pdf():
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    command = take_command()
    if 'select my book' in command:
        try:
            book= askopenfilename()
            pdfreader=PyPDF2.PdfFileReader(book)
            pages=pdfreader.numPages
            print(f'The total number of pages is :{pages}')
            speak(f'The total number of pages is :{pages}')
            print(f'what do you want to listen  single or Multile pages? ')
            speak(f'what do you want to listen  single or Multile pages? ')
            if 'single' in command:
                print('From which page you  want to play? ')
                speak('From which page you  want to play? ')
                time.sleep(3)
                page =take_command()
                print(page)
                try:
                    page = pdfreader.getPage(page)
                    speak('here are you go..')
                    speak(page)
                except:
                    pass
            elif 'multiple' in command:
                print("Enter your starting page: ")
                speak("Enter your starting page: ")
                time.sleep(3)
                start =take_command()
                print("Enter your ending page: ")
                speak("Enter your ending page: ")
                time.sleep(3)
                end = command
                try:
                    for num in range(start, end):
                        page = pdfreader.getPage(num)
                        text = page.extractText()
                        print('here are you go')
                        speak(text)
                except :
                    pass
                else:
                    print('Enter your choice properly')
                    speak('Enter your choice properly')
        except :
            pass

    elif 'exit' in command:
        exit()
    elif 'can you hear me' in command:
        speak('yes i can hear you')




if __name__ == '__main__':

    while True:
        run_pdf()


