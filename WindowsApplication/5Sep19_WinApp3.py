from tkinter import *

window = Tk()

def Add():
    r1 = e1_value.get()
    r2 = e2_value.get()
    r3 = int(r1) + int(r2)
    t1.insert(END, r3)
    print(r3)
    print("Success")

def Mul():
    r1 = e1_value.get()
    r2 = e2_value.get()
    r3 = int(r1) * int(r2)
    t1.insert(END, r3)



e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=2)

b1 = Button(window, text=" + ", command=Add)
# b1.pack()
b1.grid(row=0, column=3, rowspan=2)

b2 = Button(window, text=" * ", command=Mul)
# b1.pack()
b2.grid(row=0, column=4, rowspan=2)


t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=5)

window.mainloop()

# import tkinter
#
# window = tkinter.Tk()
#
# b1 = tkinter.Button
#
# window.mainloop()