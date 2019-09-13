from tkinter import *

top = Tk()

C = Canvas(top, bg="blue", height=500, width=500)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=50, extent=300, fill="red")
line = C.create_line(10,10,200,200,fill='white')
print(coord)

C.pack()
top.mainloop()