from tkinter import Tk, Button


def klik_op_de_knop():
    # Deze functie verandert de tekst van knop2
    knop2["text"] = "\U0001F609"


venster = Tk()
venster.title("memory")
venster.resizable(width=False, height=False)

# In knop1 staat een emoji
knop1 = Button(venster, width=5, height=5, text="\U0001F609")
knop1.grid(row=0, column=0)

# In knop2 staat niets. Als we op knop2 klikken wordt de functie "klik_op_de_knop" uitgevoerd
knop2 = Button(venster, width=5, height=5, command=klik_op_de_knop)
knop2.grid(row=0, column=1)

venster.mainloop()
