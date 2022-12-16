""" Memory """
from tkinter import Tk, Button, messagebox

def klik_op_de_knop():
    messagebox.showinfo("Hallo", "Goed geklikt!")

root = Tk()
root.title('memory')
root.resizable(width=False, height=False)

knop1 = Button(root, command=klik_op_de_knop, width=5, height=5)
knop1.grid(column=0, row=0)
knop2 = Button(root, width=5, height=5)
knop2.grid(column=1, row=0)

root.mainloop()
