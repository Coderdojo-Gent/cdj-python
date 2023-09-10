from tkinter import Tk, Button
import time
import random


def klik_op_de_knop(x, y):
    global eerste_knop

    # Dit is de knop (Button) waar op geklikt is
    knop = knoppen[x, y]
    # Dit is de emoji die bij deze knop hoort
    emoji = knop_symbolen[x, y]
    # Nu veranderen we de text van die knop met de emoji
    knop["text"] = emoji
    knop.update()

    # Als we weten wat de eerste knop was
    if eerste_knop:
        # Als de 2 knoppen niet dezelfde emoji hebben
        if eerste_knop["text"] != knop["text"]:
            time.sleep(1.0)
            eerste_knop["text"] = ""
            knop["text"] = ""
        # Vergeet de eerste knop terug
        eerste_knop = None
    else:
        # Onthou wat de eerste knop was
        eerste_knop = knop


symbolen = [
    "\U0001F609",  # winking face
    "\U0001F922",  # nauseated face
    "\U0001F636",  # face without mouth
    "\U0001F913",  # nerd face
    "\U0001F971",  # yawning face
    "\U0001F61B",  # face with tongue
    "\U0001F631",  # face screaming in fear
    "\U0001F633",  # flushed face
    "\U0001F60E",  # smiling face with sunglasses
    "\U0001F973",  # partying face
    "\U0001F976",  # cold face
    "\U0001F975",  # hot face
]
symbolen.extend(symbolen)
random.shuffle(symbolen)

# Eerst maken we een basis venster voor onze hele applicatie
venster = Tk()
# Hiermee stellen we de titel in die bovenaan het venster te zien zal zijn
venster.title("memory")
# Hiermee zorgen we dat zowel de breedte (width) and de hoogte (height) van het venster
# niet kunnen worden aangepast (resize)
venster.resizable(width=False, height=False)

eerste_knop = None
knoppen = {}
knop_symbolen = {}

for x in range(4):
    for y in range(6):
        knop = Button(
            venster, width=5, height=5, command=lambda x=x, y=y: klik_op_de_knop(x, y)
        )
        knop.grid(row=x, column=y)

        knoppen[x, y] = knop
        knop_symbolen[x, y] = symbolen.pop()

# Hiermee starten we het programma
venster.mainloop()
