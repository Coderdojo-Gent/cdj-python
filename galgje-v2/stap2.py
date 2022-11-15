"""Galgje V2 Stap 2"""
import random

with open("OpenTaal-210G-basis-gekeurd.txt") as bestand:
    woorden_lijst = bestand.read().splitlines()

goede_woorden = []

for woord in woorden_lijst:
    if woord.isalpha() and woord.islower() and woord.isascii():
        goede_woorden.append(woord)

print(random.choice(goede_woorden))
