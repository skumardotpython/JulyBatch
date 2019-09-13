# !/usr/bin/python3
from tkinter import *

root = Tk( )

def Calculalte():
    pass


e1 = Entry(root)
e1.pack

var = 0
for r in range(3):
    for c in range(3):
        var = var + 1
        print(c, end=' ')
        Button(root, border=1, text=str(var), command=Calculalte).grid(row=r, column=c)


root.mainloop()