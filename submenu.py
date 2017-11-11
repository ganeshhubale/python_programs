import tkinter
from tkinter import Menu
def hello():
    print("hello")

root = tkinter.Tk()
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)

menu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="open", command=hello)
submenu.add_command(label="save", command=hello)
submenu.add_separator()
submenu.add_command(label="exit", command=hello)

root.mainloop()

