"""Galgje Stap 3"""

woord = "galgje"
tonen = ["*", "*", "*", "*", "*", "*"]

while True:
    print(tonen)
    gok = input("Raad een letter of het hele woord: ")

    if gok == woord:
        break

    if gok in woord:
        print(gok + " zit in het woord!")
    else:
        print(gok + " zit NIET in het woord!")

    for positie, letter in enumerate(woord):
        if gok == letter:
            tonen[positie] = letter

    if "*" not in tonen:
        break

print("Goed geraden! Het woord was: " + woord)
