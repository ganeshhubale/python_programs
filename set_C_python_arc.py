from tkinter import *
master=Tk()
master.geometry("700x700")

C=Canvas(master,bg="blue",height="550",width="550")
coord=10,50,240,210
arc=C.create_arc(coord,start=0,extent=150,fill="red")
C.pack()
master.mainloop()


