""" Memory """
import random
import time
from tkinter import Tk, Button, DISABLED, font


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
        # We doen enkel iets als er niet 2 keer op dezelfde knop is geklikt
        if eerste_knop != knop:
            # Als de 2 knoppen niet dezelfde emoji hebben
            if eerste_knop["text"] != knop["text"]:
                time.sleep(1.0)
                eerste_knop["text"] = ""
                knop["text"] = ""
            # Als de 2 knoppen WEL dezelfe emoji hebben mogen ze de functie niet meer uitvoeren
            else:
                eerste_knop["command"] = DISABLED
                knop["command"] = DISABLED
            # Vergeet de eerste knop terug
            eerste_knop = None
    else:
        # Onthou wat de eerste knop was
        eerste_knop = knop


venster = Tk()
venster.title("memory")
venster.resizable(width=False, height=False)

eerste_knop = None
knoppen = {}
knop_symbolen = {}
# https://unicode.org/emoji/charts/full-emoji-list.html
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

for x in range(4):
    for y in range(6):
        knop = Button(
            command=lambda x=x, y=y: klik_op_de_knop(x, y),
            width=5,
            height=3,
            font=font.Font(size=32),
        )
        knop.grid(row=x, column=y)
        knoppen[x, y] = knop
        knop_symbolen[x, y] = symbolen.pop()

venster.mainloop()
