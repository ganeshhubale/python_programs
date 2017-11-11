import tkinter
from tkinter import messagebox
from tkinter import Frame
from tkinter import Menu
top = tkinter.Tk()

frame = Frame(top, width=512, height=512, bg="blue")
frame.pack()

bottomframe = Frame(frame, bg ="blue")
bottomframe.pack()
def hello():
    print("its menu magic")
def msg():
    messagebox.showinfo("Hello python", "this Button is RED")

def msg1():
    messagebox.showinfo("hello python", "this button is green")

redbutton = tkinter.Button(top, text="Red", fg="red", command = msg)
redbutton.pack()

greenbutton = tkinter.Button(top, text="green", fg="green", command = msg1)
greenbutton.pack()

top.mainloop()
