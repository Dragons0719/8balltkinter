# Magic 8 Ball in Tkinter v2.1
# August 18
# Created by Elijah Rothenberger

from ast import Lambda
from distutils.cmd import Command
from tkinter import *
import random as r
from tkinter import Label
import time as t
from tkinter.font import BOLD

def close():
    start.destroy()

def begin():
    def clear():
        label1.config(text="")
        user_entry.delete(0, END)
    def answer():
        label1.config(text=f"{r.choice(answers)}")
    def exit():
        start.destroy()

   

    root = Toplevel()
    root.attributes('-fullscreen',True)
    root.title('Magic 8 Ball')
    root.config(bg='light green')
    message = Label(root, font=('Goudy Old Style', 30), text='Ask the Magic 8 Ball a yes/no question'
                                                   '\n in the space below!', bg='light green')
    message.place(x=650, y=15)
    user_entry = Entry(root, font=('Goudy Old Style', 30), bg='black', fg='light green')
    user_entry.place(x=760, y=200)
    button1 = Button(root, font=('Goudy Old Style', 20), text='        Enter        ', bg='black', fg='white', command=answer)
    button1.place(x=865, y=400)
    button2 = Button(root, font=('Goudy Old Style', 20), text='        Clear        ', bg='black', fg='white', command=clear)
    button2.place(x=865, y=500)
    button3 = Button(root, font=('Goudy Old Style', 20), text='        Exit        ', bg='black', fg='white', command=exit)
    button3.place(x=872, y=600)
    label1 = Label(root, font=('Goudy Old Style', 25), text="", bg='light green')
    label1.place(x=886, y=300)
    answers = ["   Possibly", "  Ask Again", "     Yes", "Definitely Not", "   Idk bro", "      No", "¯\_(ツ)_/¯"]
    rand_value = int(r.random() * len(answers))
    root.mainloop()




start = Tk()
start.title('Welcome!')
start.attributes('-fullscreen',True)
start.config(bg='light green')
welcome = Label(start, bg='light green', font=('Goudy Old Style', 30), text='Welcome to the magic 8 ball!\nPress the start button to begin!')
welcome.place(x=700, y=100)
startbut = Button(start,font=('Goudy Old Style', 25), text='Start!', bg='black', fg='white', command=begin)
startbut.place(x=885, y=300)
closebut = Button(start, bg='black', fg='white', text='Close!',font=('Goudy Old Style', 25), command=close)
closebut.place(x=880, y=400)
start.mainloop()
