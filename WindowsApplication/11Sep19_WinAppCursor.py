# !/usr/bin/python3
from tkinter import *

top = Tk()

B1 = Button(top, text ="circle", relief=RAISED, \
            cursor="circle")
B2 = Button(top, text ="plus", relief=RAISED, \
            cursor="clock")
B1.pack()
B2.pack()
top.mainloop()