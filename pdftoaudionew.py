import PyPDF2
import PyPDF2 as reader
from gtts import *
import os
import tkinter
from tkinter.filedialog import *
from tkinter import messagebox
from playsound import playsound
window = tkinter.Tk()
window.title("Pdf to Hindi Audio")
window.geometry("400x200")
global book
def entryFile():
    global book
    global filename
    book = askopenfilename()
    filename = str(book)
def convertfile():
    global filename
    with open(filename, 'rb') as file:
        pdf = reader.PdfFileReader(filename)
        print(pdf.numPages)
        for num in range(pdf.numPages):
            page = pdf.getPage(num)
            text = page.extractText()
            print(text)
            tts = gTTS(str(text), lang='hi')
            # tts.save(num + ".mp3")
            savefile = f'{str(num)}.mp3'
            tts.save(savefile)
def exit():
    tkinter.messagebox.askyesno("Exit Pop","You want to exit")
    window.destroy()

    return


label1 = Label(window,text="Please select the file",bg="grey")
label1.grid(row=0,column=0,ipadx=12,ipady=10)
user_value = StringVar()
b1 = Button(window,command=entryFile,text="Select the location of the file")
b1.grid(row=0,column=1,ipadx=12,ipady=10,)
b2 = Button(window,command=convertfile,text="convert")
b2.grid(row=1,column=1,ipadx=12,ipady=10,)

b3 = Button(window,command=exit,text="exit")
b3.grid(row=2,column=1,ipadx=12,ipady=10,)
"""


book = askopenfilename()
filename = str(book)
with open(filename,'rb') as file:
    pdf = reader.PdfFileReader(filename)
    print(pdf.numPages)
    for num in range(pdf.numPages):
        page = pdf.getPage(num)
        text = page.extractText()
        print(text)
        tts = gTTS(str(text),lang='hi')
       # tts.save(num + ".mp3")
        savefile = f'{str(num)}.mp3'
        tts.save(savefile)
"""

window.mainloop()