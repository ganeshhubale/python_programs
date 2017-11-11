from tkinter import *
from tkinter import colorchooser

master=Tk()
master.geometry("700x700")

def getColor():
    color_choice=colorchooser.askcolor()[1]
    l1=Label(master,text="you have choose this color",bg=color_choice,fg="blue")
    l1.pack()

b1=Button(master,text="choose",command=getColor)
b1.pack()
master.mainloop()
