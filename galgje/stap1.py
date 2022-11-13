"""Galgje Stap 1"""

woord = "galgje"

while True:
    gok = input("Raad een letter: ")
    if gok in woord:
        print(gok + " zit in het woord!")
    else:
        print(gok + " zit NIET in het woord!")
