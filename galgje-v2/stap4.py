"""Galgje V2 Stap 4"""
import random

WOORD_LENGTE = 5
START_LEVENS = 10

with open("OpenTaal-210G-basis-gekeurd.txt") as bestand:
    woorden_lijst = bestand.read().splitlines()

goede_woorden = []

for woord in woorden_lijst:
    if (
        woord.isalpha()
        and woord.islower()
        and woord.isascii()
        and len(woord) == WOORD_LENGTE
    ):
        goede_woorden.append(woord)

woord = random.choice(goede_woorden)
tonen = ["*", "*", "*", "*", "*"]
levens = START_LEVENS

while levens > 0:
    print()
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
