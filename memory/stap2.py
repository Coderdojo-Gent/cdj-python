from tkinter import Tk, Button

# Eerst maken we een basis venster voor onze hele applicatie
venster = Tk()

# Hiermee stellen we de titel in die bovenaan het venster te zien zal zijn
venster.title("memory")

# Hiermee zorgen we dat zowel de breedte (width) and de hoogte (height) van het venster
# niet kunnen worden aangepast (resize)
venster.resizable(width=False, height=False)

for x in range(4):
    for y in range(6):
        knop = Button(width=5, height=5, text=f"knop ({x}, {y})")
        knop.grid(row=x, column=y)


# Hiermee starten we het programma
venster.mainloop()
