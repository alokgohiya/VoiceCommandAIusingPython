import tkinter
from tkinter import font
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from tkinter.ttk import *
from PIL import ImageTk,Image
import webbrowser

top=tkinter.Tk()
top.title("Alice")
top.iconbitmap(r'C:\Users\LENOVO\OneDrive\Documents\alice.ico')

top.geometry('400x200+700+300')
top.minsize(400,200)
top.maxsize(400,200)
img=Image.open("jarvis.jpg")
photo=ImageTk.PhotoImage(img)
bglbl=Label(top,image=photo).pack()


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
def talk(taxt):
    engine.say(taxt)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                

    except:
        pass
    return command

def run_alexa():
    command=take_command()
    
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I %M %p")
        
        talk("Current time is"+ time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
    
        talk(info)
    elif 'joke' in command:
        jokes=pyjokes.get_joke()
        talk(jokes)
    elif 'who i am' in command:
        talk('Your name is aalok and you are my owner')
    elif 'thank you' in command:
        talk("you are welcome")
    elif  'who are you' in command:
        talk("my name is alice and i am aloks personal assistant")
    elif 'exit' in command:
        top.destroy()
    elif 'open facebook' in command:
        webbrowser.open("https://www.facebook.com",new=1)
    elif 'open instagram' in command:
        webbrowser.open("https://www.instagram.com",new=1)
    elif 'open twitter' in command:
        webbrowser.open("https://www.twitter.com",new=1)
    elif 'open google' in command:
        webbrowser.open("https://www.google.com",new=1)
    elif 'open whatsapp' in command:
        webbrowser.open("https://www.whatsapp.com")
   
   

    else:
        talk("Sorry, I'm not able to help with this one.")


lbl=Label(top,text="Alice",font=('calibari',10,'bold'),foreground="grey",background="black").place(x=165,y=30)
btn=tkinter.Button(top,text="Search",background="lightblue",font =
               ('calibri', 10, 'italic'),fg="grey5",command=run_alexa).place(x=165,y=110)
lbl1=Label(top,text="Designed by Alok gohiya",font=('calibari',7,'italic'),foreground="grey",background="black").place(x=130,y=170)
top.mainloop()