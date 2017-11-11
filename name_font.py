from tkinter import *

master = Tk()
master.geometry("300x300")
w = Label(master,text="Today is external",fg="black").pack(padx=5,pady=10,side=LEFT)
b = Label(master,text="python is simple language",fg="red").pack(padx=15,pady=40,side=LEFT)
c = Label(master,text="welcome to RIT").pack(padx=15,pady=20,side=LEFT)
master.mainloop()

