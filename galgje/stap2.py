"""Galgje Stap 2"""

woord = "galgje"
tonen = ["*", "*", "*", "*", "*", "*"]

while True:
    print(tonen)
    gok = input("Raad een letter: ")

    if gok in woord:
        print(gok + " zit in het woord!")
    else:
        print(gok + " zit NIET in het woord!")

    for positie, letter in enumerate(woord):
        if gok == letter:
            tonen[positie] = letter
