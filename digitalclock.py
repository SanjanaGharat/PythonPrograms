from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital Clock")

def get_time():
   timeVar = time.strftime("%I:%M:%S:%p")
   clock.config(text=timeVar)
   clock.after(200,get_time)

clock=Label(master,font=("calibri",90),bg="black",fg="lawn green")

clock.pack()
get_time()
master.mainloop()