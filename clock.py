from tkinter import *
from time import strftime

window = Tk()
window.title("clock")

def time():
    string = strftime('%H:%M:%S    %d-%m-%Y')
    Label.config(text = string)
    Label.after(1000,time)
    
    
Label = Label(window,font = ("ds-digital",70),background = "black",foreground = "cyan")
Label.pack(anchor = 'center')
time()

mainloop()


