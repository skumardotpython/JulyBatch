from tkinter import *
from tkinter import messagebox

top = Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

def CheckButton1():
    if(CheckVar1.get() == 1):
        msg=messagebox.showinfo( "CheckBox Alert", "Music is Selected")
    else:
        msg=messagebox.showinfo( "CheckBox Alert", "Music is DeSelected")

C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, underline = 1, command = CheckButton1,)

C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
top.mainloop()