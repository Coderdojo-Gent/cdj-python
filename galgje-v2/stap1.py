"""Galgje V2 Stap 1"""
import random

with open("OpenTaal-210G-basis-gekeurd.txt") as bestand:
    woorden_lijst = bestand.read().splitlines()

print(random.choice(woorden_lijst))
