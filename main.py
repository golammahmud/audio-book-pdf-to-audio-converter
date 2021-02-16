from tkinter import EXCEPTION

import pyttsx3
import PyPDF2
from tkinter.filedialog import *



talk=pyttsx3.init('sapi5')
# book= askopenfilename()
# pdfreader=PyPDF2.PdfFileReader(book)
# pages=pdfreader.numPages



def speak(text):
    talk.say(text)
    talk.runAndWait()



def run_pdf():
   print('do you want to play your pdf file ....please select your file')
   file=input('write "open file" to open your pdf file:')
   if 'open file' in file:
       book = askopenfilename()
       pdfreader=PyPDF2.PdfFileReader(book)
       pages=pdfreader.numPages
       print(f'The total number of pages is :{pages}')
       print(f'what do you want to listen  single or Multile pages? ')
       take_input_pages = input("Enter your choice: ")

       if 'single' in take_input_pages:
           print('From which page you  want to play? ')
           page = int(input("Enter your page number:"))
           try:
               page = pdfreader.getPage(page)
               print('here are you go')
               speak(page)
           except EXCEPTION as e:
               print(e)
       elif 'multiple' in take_input_pages:
           start = int(input("Enter your starting page: "))
           end = int(input("Enter your ending page: "))
           try:
               for num in range(start, end):
                   page = pdfreader.getPage(num)
                   text = page.extractText()
                   print('here are you go')
                   speak(text)
           except EXCEPTION as e:
               print(e)
       elif 'exit' in take_input_pages:
           exit()

       else:
           print('Enter your choice properly')
   elif 'exit' in file or 'no' in file or 'cencel' in file:
       take_input=input('are you sure you want to exit:')
       if 'yes' in take_input:
           exit()
       else:
           pass


if __name__ == '__main__':

    while True:
        run_pdf()


