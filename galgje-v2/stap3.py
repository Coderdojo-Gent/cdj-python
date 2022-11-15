"""Galgje V2 Stap 3"""
import random

WOORD_LENGTE = 5

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

print(random.choice(goede_woorden))
