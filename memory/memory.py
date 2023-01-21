""" Memory """
import random
import time
from tkinter import Tk, Button, DISABLED, font

def toon_symbool (x, y):
    print(f"toon_symbool({x}, {y})")
    global eerste
    global vorigeX, vorigeY
    knoppen[x, y]['text'] = knop_symbolen[x, y]
    knoppen[x, y].update()
    if eerste:
        vorigeX = x
        vorigeY = y
        eerste = False
    elif vorigeX != x or vorigeY != y:
        if knoppen[vorigeX, vorigeY]['text'] != knoppen[x, y]['text']:
            time.sleep(1.0)
            knoppen[vorigeX, vorigeY]['text']=''
            knoppen[x, y]['text'] = ''
        else:
            knoppen[vorigeX, vorigeY]['command'] = DISABLED
            knoppen[x, y]['command'] = DISABLED
        eerste = True


root = Tk()
root.title('memory')
root.resizable(width=False, height=False)

knoppen = {}
eerste = True
vorigeX = 0
vorigeY = 0
knop_symbolen = {}
# https://unicode.org/emoji/charts/full-emoji-list.html
symbolen = ["\N{winking face}",
            "\N{nauseated face}",
            "\N{face without mouth}",
            "\N{nerd face}",
            "\N{yawning face}",
            "\N{face with tongue}",
            "\N{face screaming in fear}",
            "\N{flushed face}",
            "\N{smiling face with sunglasses}",
            "\N{partying face}",
            "\N{cold face}",
            "\N{hot face}"]

symbolen.extend(symbolen)
random.shuffle(symbolen)

for x in range(6):
    for y in range(4):
        knop = Button(command=lambda x=x, y=y: toon_symbool(x, y), width=5, height=3, font=font.Font(size=32))
        knop.grid(column=x, row=y)
        knoppen[x, y] = knop
        knop_symbolen[x, y] = symbolen.pop()
        knoppen[x, y]["text"] = knop_symbolen[x, y]

root.mainloop()
