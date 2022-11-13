"""Galgje Stap 4"""

woord = "galgje"
tonen = ["*", "*", "*", "*", "*", "*"]
levens = 10

while levens > 0:
    print(tonen)
    print("Je hebt nog " + str(levens) + " levens.")
    gok = input("Raad een letter of het hele woord: ")

    if gok == woord:
        break

    if gok in woord:
        print(gok + " zit in het woord!")
    else:
        print(gok + " zit NIET in het woord!")
        levens = levens - 1

    for positie, letter in enumerate(woord):
        if gok == letter:
            tonen[positie] = letter

    if "*" not in tonen:
        break

if levens > 0:
    print("Goed geraden! Het woord was: " + woord)
else:
    print("Game Over! Het juiste woord was: " + woord)
