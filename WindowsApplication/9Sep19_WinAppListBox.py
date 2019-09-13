from tkinter import *

parent = Tk()

valores = StringVar()
valores.set("Carro Coche Moto Bici Triciclo Patineta Patin Patines Lancha Patrullas")

lst = Listbox(parent, listvariable=valores, selectmode=MULTIPLE)
lst.insert(0, "One"),
lst.insert(1, "Two")
lst.insert(2, "Two")
lst.insert(3, 'Three')

lst.pack()

parent.mainloop()