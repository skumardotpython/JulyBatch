# !/usr/bin/python3
from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root)

for line in range(100):
    mylist.insert(END, "This is line number " + str(line))
mylist.pack( side = LEFT)

# scrollbar.config( command = mylist.yview )
mainloop()