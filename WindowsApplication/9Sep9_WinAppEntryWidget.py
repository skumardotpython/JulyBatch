# !/usr/bin/python3
from tkinter import *

top = Tk()

L1 = Label(top, text="Please enter the user Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)


top.mainloop()