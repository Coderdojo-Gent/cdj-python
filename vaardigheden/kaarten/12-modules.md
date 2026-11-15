# Modules importeren

Python heeft heel veel extra functies, verpakt in *modules*. Voor je een module gebruikt, moet je ze **importeren**, helemaal bovenaan je programma.

## Zo werkt het

```python
import random

getal = random.randint(1, 10)    # willekeurig getal van 1 tot en met 10
print(getal)
```

Na `import random` schrijf je de naam van de module, een punt en de functie: `random.randint()`.

Je kan ook 1 functie importeren. Dan schrijf je de naam van de module er niet meer voor:

```python
from random import randrange

getal = randrange(1, 10)         # 1 tot en met 9: de 10 zit er niet bij!
```

## Handige modules (zitten al in Python)

| Code | Wat doet het? |
|---|---|
| `random.randint(1, 6)` | willekeurig getal van 1 tot en met 6 (een dobbelsteen) |
| `random.randrange(0, 10)` | willekeurig getal van 0 tot en met 9 |
| `random.random()` | willekeurig kommagetal van 0 tot 1 |
| `random.choice(lijst)` | willekeurig element uit een lijst |
| `random.shuffle(lijst)` | zet de lijst in een willekeurige volgorde |
| `time.sleep(1)` | wacht 1 seconde (na `import time`) |
| `math.sqrt(16)` | vierkantswortel: `4.0` (na `import math`) |

## Extra modules installeren met pip

Sommige modules, zoals `pygame`, zitten niet in Python. Die installeer je 1 keer, in de terminal (in VS Code onderaan):

```text
pip install pygame
```

Lukt dat niet? Probeer `python -m pip install pygame` (Windows) of `python3 -m pip install pygame` (Mac). Lukt het nog niet, vraag dan een coach.

## Let op

- Geef je eigen bestand nooit de naam van een module: `random.py`, `pygame.py`, `turtle.py`... Dan importeert Python jouw bestand in plaats van de echte module!
- `ModuleNotFoundError: No module named 'pygame'` betekent: die module is nog niet geïnstalleerd, of je hebt de naam verkeerd getypt.

## Probeer het zelf

Maak een dobbelsteen: elke keer dat de speler op Enter drukt, print je een willekeurig getal van 1 tot 6.
