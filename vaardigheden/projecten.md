# Projecten: wat moet je al kennen?

Bij elk project staat:

- **Voorkennis**: wat je best al kent voor je begint. Ken je iets niet? Lees eerst die kaart, of vraag een coach.
- **Dit leer je**: wat het project zelf uitlegt. Dat hoef je dus nog niet te kennen! De kaarten helpen je als je vastzit.
- **Eerst gedaan**: projecten die je best eerst maakt.

Kaart 18 (foutmeldingen lezen) helpt bij elk project.

## Overzicht

De getallen zijn de nummers van de [kaarten](#de-kaarten).

| Niveau | Project | Voorkennis | Dit leer je |
|---|---|---|---|
| 1 | Kennismaking met Python | geen | 1, 2, 3, 4, 5, 6, 7, 9 |
| 1 | Raad het Getal | geen | 1, 2, 3, 4, 5, 6, 7, 12 |
| 1 | Geheime Boodschappen | 1, 2, 4 | 3, 5, 6, 8 |
| 1 | Schildpad (turtle) | geen | 2, 6, 7, 9, 12, 14, 15 |
| 2 | Galgje | 1, 2, 3, 4, 5, 6 | 7, 9 |
| 2 | Waar is het ISS? | 1, 2, 6, 9, 12 | 3, 10, 14, 15 |
| 2 | Role Playing Game (RPG) | 1, 2, 4, 5, 7, 9 | 8, 10, 11 |
| 2 | Galgje Uitbreiding | Galgje, 5, 6, 9 | 8, 12, 13 |
| 3 | Memory | 2, 5, 6, 8, 9, 12 | 10, 11 |
| 3 | Snake | 2, 3, 5, 6, 7, 9, 11, 12 | 14, 16 |
| 3 | Pong | 2, 3, 5, 6, 7, 12 | 14, 16 |
| 3 | Flappy Bird | Pong of Snake, 2, 3, 5, 11, 14, 16 | 17 |

## Niveau 1: Beginner

### Kennismaking met Python

[Coderdojo Belgium Google Drive](https://drive.google.com/file/d/1s12L4sIU-WU-DM0DNQ_s6aBhFoMWQjMD)

**Voorkennis:** geen. Ervaring met Scratch helpt wel.

**Dit leer je:**

- Tekst tonen met `print()` en vragen stellen met `input()`: [1](kaarten/01-print.md), [4](kaarten/04-input.md)
- Variabelen en tekst omzetten naar een getal met `int()`: [2](kaarten/02-variabelen.md), [3](kaarten/03-rekenen.md)
- Beslissen met `if`, `elif` en `else`: [5](kaarten/05-if-elif-else.md)
- Tellen met een `for`-lus en herhalen met een `while`-lus: [6](kaarten/06-for-lus.md), [7](kaarten/07-while-lus.md)
- Een lijst met deelnemers bijhouden: [9](kaarten/09-lijsten.md)
- Een venster met een knop en figuren maken met `tkinter`, en een eerste kennismaking met `def` en `random`

### Raad het Getal

[Via Coderdojo Wijchen Noord](https://drive.google.com/file/d/1TZRLjFt4_y78Pcq89kh2_wcbAhYC0Dcm/view) (start op pagina 10)

**Voorkennis:** geen. Ervaring met Scratch helpt wel.

**Dit leer je:**

- `print()`, `input()` en variabelen: [1](kaarten/01-print.md), [4](kaarten/04-input.md), [2](kaarten/02-variabelen.md)
- Tekst omzetten naar een getal met `int()`: [3](kaarten/03-rekenen.md)
- Een willekeurig getal met `from random import randrange`: [12](kaarten/12-modules.md)
- Vergelijken met `if` en `else`: [5](kaarten/05-if-elif-else.md)
- Meerdere pogingen met een `for`-lus, en stoppen met `break`: [6](kaarten/06-for-lus.md), [7](kaarten/07-while-lus.md)

**Tip voor coaches:** de PDF vergelijkt getallen met `is`. Leer de kinderen `==` gebruiken. `randrange(1, 10)` kiest 1 tot en met 9, niet tot 10.

### Geheime Boodschappen

[geheime_boodschappen/](../geheime_boodschappen/README.md)

**Voorkennis:**

- `print()`: [1](kaarten/01-print.md)
- Variabelen: [2](kaarten/02-variabelen.md)
- `input()`: [4](kaarten/04-input.md)

**Dit leer je:**

- Rond gaan in het alfabet met `%`, en `int(input())`: [3](kaarten/03-rekenen.md)
- Letters opzoeken met `find()` en `[ ]`, `lower()`, en een nieuwe string opbouwen met `+=`: [8](kaarten/08-strings.md)
- Elke letter van een boodschap doorlopen met een `for`-lus: [6](kaarten/06-for-lus.md)
- Alleen letters versleutelen met `if ... in ...` en `else`: [5](kaarten/05-if-elif-else.md)

### Schildpad (turtle)

[turtle/Python_beginner_opdrachtjes_Turtle.pdf](../turtle/Python_beginner_opdrachtjes_Turtle.pdf)

**Voorkennis:** geen. Ervaring met Scratch helpt wel.

**Dit leer je:**

- Tekenen met een schildpad: [15](kaarten/15-turtle.md)
- Variabelen: [2](kaarten/02-variabelen.md)
- Figuren herhalen met een `for`-lus, ook een lus in een lus: [6](kaarten/06-for-lus.md)
- Een lijst met kleuren: [9](kaarten/09-lijsten.md)
- Een `while`-lus met een teller: [7](kaarten/07-while-lus.md)
- Coördinaten, `setposition()` en RGB-kleuren: [14](kaarten/14-coordinaten-en-kleuren.md)
- Willekeurige kleuren met `random.random()`: [12](kaarten/12-modules.md)

**Tip voor coaches:** de PDF gebruikt IDLE. In VS Code moet `turtle.done()` onderaan, anders gaat het venster meteen dicht.

## Niveau 2: Gevorderd

### Galgje

[galgje/](../galgje/README.md)

**Eerst gedaan:** Geheime Boodschappen of Raad het Getal is een goede voorbereiding.

**Voorkennis:**

- `print()` en tekst aan elkaar plakken met `+`: [1](kaarten/01-print.md)
- Variabelen: [2](kaarten/02-variabelen.md)
- Een getal omzetten naar tekst met `str()`: [3](kaarten/03-rekenen.md)
- `input()`: [4](kaarten/04-input.md)
- `if` en `else`, en `in` om te kijken of een letter in een woord zit: [5](kaarten/05-if-elif-else.md)
- Een `for`-lus over een string: [6](kaarten/06-for-lus.md)

**Dit leer je:**

- Een oneindige lus met `while True` en `break`, en later `while levens > 0`: [7](kaarten/07-while-lus.md)
- Een lijst met sterretjes, waarin je 1 element verandert: [9](kaarten/09-lijsten.md)
- Positie en letter samen met `enumerate()`: [6](kaarten/06-for-lus.md)
- `not in`: [5](kaarten/05-if-elif-else.md)

### Waar is het ISS?

[waar_is_het_iss/](../waar_is_het_iss/README.md)

**Eerst gedaan:** Schildpad (turtle) helpt, maar is niet nodig.

**Voorkennis:**

- `print()` en variabelen: [1](kaarten/01-print.md), [2](kaarten/02-variabelen.md)
- Een `for`-lus over een lijst: [6](kaarten/06-for-lus.md)
- Een lijst vullen met `append()`: [9](kaarten/09-lijsten.md)
- Modules importeren: [12](kaarten/12-modules.md)

**Dit leer je:**

- Data van een webservice inlezen (JSON met `urllib.request` en `json`)
- Dictionaries, en een lijst van dictionaries: [10](kaarten/10-dictionaries.md)
- Tekst omzetten naar een kommagetal met `float()`: [3](kaarten/03-rekenen.md)
- Lengte- en breedtegraad als coördinaten: [14](kaarten/14-coordinaten-en-kleuren.md)
- Een kaart tekenen met turtle: `Screen()`, `bgpic()`, `goto()` en `write()`: [15](kaarten/15-turtle.md)

**Tip voor coaches:** `turtle` zit al in Python. `pip install PythonTurtle` uit de README is niet nodig.

### Role Playing Game (RPG)

[RPG - raspberrypi.org](https://projects.raspberrypi.org/nl-NL/projects/rpg/0)

**Eerst gedaan:** Galgje.

**Voorkennis:**

- `print()`, variabelen en `input()`: [1](kaarten/01-print.md), [2](kaarten/02-variabelen.md), [4](kaarten/04-input.md)
- `if`, `and` en `in`: [5](kaarten/05-if-elif-else.md)
- `while True` en `break`: [7](kaarten/07-while-lus.md)
- Lijsten (de inventaris): [9](kaarten/09-lijsten.md)

**Dit leer je:**

- Een kaart van kamers maken met dictionaries in een dictionary: [10](kaarten/10-dictionaries.md)
- Een commando opsplitsen met `.lower().split()`: [8](kaarten/08-strings.md)
- Bestaande code lezen en uitbreiden, ook een functie als `toonInstructies()`: [11](kaarten/11-functies.md)

### Galgje Uitbreiding

[galgje-v2/](../galgje-v2/README.md)

**Eerst gedaan:** Galgje. Je gebruikt je code van Galgje opnieuw.

**Voorkennis:**

- `if` met `and`: [5](kaarten/05-if-elif-else.md)
- Een `for`-lus over een lijst: [6](kaarten/06-for-lus.md)
- Een nieuwe lijst vullen met `append()`: [9](kaarten/09-lijsten.md)

**Dit leer je:**

- Een bestand inlezen met `with open()` en `splitlines()`: [13](kaarten/13-bestanden.md)
- Woorden filteren met `isalpha()`, `islower()`, `isascii()` en `len()`: [8](kaarten/08-strings.md)
- Een willekeurig woord kiezen met `import random` en `random.choice()`: [12](kaarten/12-modules.md)
- Constanten zoals `WOORD_LENGTE`: [2](kaarten/02-variabelen.md)

## Niveau 3: Vergevorderd

### Memory

[memory/](../memory/README.md)

**Eerst gedaan:** een project van niveau 2, bv. Galgje.

**Voorkennis:**

- Variabelen: [2](kaarten/02-variabelen.md)
- `if` en `else`, ook een `if` in een `if`: [5](kaarten/05-if-elif-else.md)
- `for` met `range()`, en een lus in een lus: [6](kaarten/06-for-lus.md)
- f-strings: [8](kaarten/08-strings.md)
- Lijsten: [9](kaarten/09-lijsten.md)
- `import random`: [12](kaarten/12-modules.md)

**Dit leer je:**

- Functies maken met `def` en argumenten, en `global`: [11](kaarten/11-functies.md)
- `None` gebruiken voor "nog niets"
- Een venster met knoppen maken met `tkinter`
- Een dictionary met `(x, y)`-posities als sleutel: [10](kaarten/10-dictionaries.md)
- `extend()`, `random.shuffle()` en `pop()` op een lijst: [9](kaarten/09-lijsten.md), [12](kaarten/12-modules.md)
- Een functie meegeven aan een knop met `lambda` (dat stukje krijg je gewoon)

### Snake

[snake/pygame cursus.pdf](../snake/pygame%20cursus.pdf)

**Eerst gedaan:** een project van niveau 2. De cursus zegt zelf dat je de basis van Python moet kennen.

**Voorkennis:**

- Variabelen en rekenen, ook `round()`: [2](kaarten/02-variabelen.md), [3](kaarten/03-rekenen.md)
- `if`, `elif`, `and`, `or` en `!=`: [5](kaarten/05-if-elif-else.md)
- `for`- en `while`-lussen: [6](kaarten/06-for-lus.md), [7](kaarten/07-while-lus.md)
- Lijsten met `append()`, `len()` en `del`: [9](kaarten/09-lijsten.md)
- Functies met argumenten: [11](kaarten/11-functies.md)
- `import random` en `pip install pygame`: [12](kaarten/12-modules.md)

**Dit leer je:**

- De game loop van pygame: events, tekenen, `update()` en de klok: [16](kaarten/16-pygame.md)
- Coördinaten en RGB-kleuren: [14](kaarten/14-coordinaten-en-kleuren.md)
- Tekst op het scherm zetten
- Een lijst van lijsten (de slang), en `slang[:-1]`: alles behalve het laatste element: [9](kaarten/09-lijsten.md)

**Tip voor coaches:** de installatie-uitleg in de PDF is verouderd (Python 2.7 en 3.5). Gebruik gewoon `pip install pygame` (kaart 12). In de PDF zijn groen en blauw omgewisseld: blauw is `(0, 0, 255)`.

### Pong

[pong/](../pong/README.md)

**Eerst gedaan:** een project van niveau 2.

**Voorkennis:**

- Variabelen: [2](kaarten/02-variabelen.md)
- Rekenen met `/`, `*` en `int()`: [3](kaarten/03-rekenen.md)
- `if`, `and`, `or` en `not`: [5](kaarten/05-if-elif-else.md)
- `for`- en `while`-lussen: [6](kaarten/06-for-lus.md), [7](kaarten/07-while-lus.md)
- `import` en `pip install pygame`: [12](kaarten/12-modules.md)

**Dit leer je:**

- De game loop van pygame: [16](kaarten/16-pygame.md) (de README verwijst naar Snake voor de uitleg, deze kaart kan ook)
- Coördinaten, RGB-kleuren en constanten: [14](kaarten/14-coordinaten-en-kleuren.md), [2](kaarten/02-variabelen.md)
- Een bal laten bewegen en botsen met `snelheid * -1`
- Toetsen lezen met `KEYDOWN` en `key.get_pressed()`: [16](kaarten/16-pygame.md)

### Flappy Bird

[flappy-bird/](../flappy-bird/README.md)

**Eerst gedaan:** Pong of Snake. De README begint meteen met de basiscode van een pygame-spel.

**Voorkennis:**

- Variabelen en constanten: [2](kaarten/02-variabelen.md)
- Rekenen met `//` en `int()`: [3](kaarten/03-rekenen.md)
- `if`, `elif`, `and`, `or` en `not`: [5](kaarten/05-if-elif-else.md)
- Functies met argumenten en standaardwaarden: [11](kaarten/11-functies.md)
- Coördinaten: [14](kaarten/14-coordinaten-en-kleuren.md)
- De game loop van pygame: [16](kaarten/16-pygame.md)

**Dit leer je:**

- Klassen, objecten en subklassen: [17](kaarten/17-klassen.md)
- Sprites en sprite-groepen, en botsingen met `groupcollide()`
- Afbeeldingen laden, omdraaien en tonen met `blit()`
- Iets doen om de zoveel tijd met `pygame.time.get_ticks()`
- Een willekeurige opening met `random.randrange()`: [12](kaarten/12-modules.md)
- Afbeeldingen afwisselen met `itertools.cycle()`

## Nog niet af

Tetris en Gezicht herkennen zijn nog niet af en staan daarom niet in deze lijst.

## De kaarten

1. [Tekst tonen met print()](kaarten/01-print.md)
2. [Variabelen](kaarten/02-variabelen.md)
3. [Getallen en rekenen](kaarten/03-rekenen.md)
4. [Vragen stellen met input()](kaarten/04-input.md)
5. [Beslissen met if, elif en else](kaarten/05-if-elif-else.md)
6. [Herhalen met een for-lus](kaarten/06-for-lus.md)
7. [Herhalen met een while-lus](kaarten/07-while-lus.md)
8. [Werken met tekst (strings)](kaarten/08-strings.md)
9. [Lijsten](kaarten/09-lijsten.md)
10. [Dictionaries (woordenboeken)](kaarten/10-dictionaries.md)
11. [Functies](kaarten/11-functies.md)
12. [Modules importeren](kaarten/12-modules.md)
13. [Bestanden lezen](kaarten/13-bestanden.md)
14. [Coördinaten en kleuren](kaarten/14-coordinaten-en-kleuren.md)
15. [Tekenen met turtle](kaarten/15-turtle.md)
16. [Een spel met pygame: de game loop](kaarten/16-pygame.md)
17. [Klassen en objecten](kaarten/17-klassen.md)
18. [Foutmeldingen lezen](kaarten/18-foutmeldingen.md)
