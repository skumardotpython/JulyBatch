from tkinter import *

parent = Tk()

strVariable = StringVar();
strVariable.set('New Variable Value')

lab = Label(parent, textvariable = strVariable)
lab.pack()



parent.mainloop()