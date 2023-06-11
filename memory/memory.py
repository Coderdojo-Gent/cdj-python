""" Memory """
import random
import time
from tkinter import Tk, Button, DISABLED, font


def toon_symbool(x, y):
    print(f"toon_symbool({x}, {y})")
    global eerste
    global vorigeX, vorigeY
    knoppen[x, y]["text"] = knop_symbolen[x, y]
    knoppen[x, y].update()
    if eerste:
        vorigeX = x
        vorigeY = y
        eerste = False
    elif vorigeX != x or vorigeY != y:
        if knoppen[vorigeX, vorigeY]["text"] != knoppen[x, y]["text"]:
            time.sleep(1.0)
            knoppen[vorigeX, vorigeY]["text"] = ""
            knoppen[x, y]["text"] = ""
        else:
            knoppen[vorigeX, vorigeY]["command"] = DISABLED
            knoppen[x, y]["command"] = DISABLED
        eerste = True


venster = Tk()
venster.title("memory")
venster.resizable(width=False, height=False)

knoppen = {}
eerste = True
vorigeX = 0
vorigeY = 0
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
            command=lambda x=x, y=y: toon_symbool(x, y),
            width=5,
            height=3,
            font=font.Font(size=32),
        )
        knop.grid(row=x, column=y)
        knoppen[x, y] = knop
        knop_symbolen[x, y] = symbolen.pop()

venster.mainloop()
