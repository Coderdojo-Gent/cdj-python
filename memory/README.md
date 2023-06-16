# Memory

* Level: 3 - Vergevorderd
* Onderwerpen: tkinter, functies, lussen, dictionaries

In deze opdracht maken we een eenvoudige versie van het spelletje Memory. Hierbij moeten de spelers om beurt proberen 2 "kaartjes" met dezelfde afbeelding om te draaien.

## De Spelregels

(meer info: https://nl.wikipedia.org/wiki/Memory_(spel))

* Het spel wordt gespeeld met 2 spelers
* Het speelvlak bestaat uit 4 rijen van telkens 6 kaarten
* Elke kaart heeft langs een kant een figuur
* Elk figuur komt op precies 2 kaarten voor
* Bij de start van het spel zijn alle kaarten gedraaid zodat de figuren niet zichtbaar zijn
* Een speler mag 2 kaarten kiezen die worden omgedraaid
  * Als de figuren hetzelfde zijn krijgt de speler een punt en mag hij nog eens spelen
  * Als de figuren verschillende zijn worden de kaarten terug omgedraaid en gaan de beurt naar de andere speler

## Stap 0: Wat is een functie?

Een _functie_ in Python is als een speciale doos waar je een aantal instructies in kunt stoppen. Je kunt deze doos een naam geven, zoals bvb. `hallo`. Telkens wanneer je die naam noemt, weet Python welke instructies erin zitten en voert het die uit.

Een functie in Python kan ook _argumenten_ hebben. Denk aan argumenten als extra informatie die je aan de functie kunt geven, zodat deze ermee kan werken en het resultaat kan aanpassen op basis van die informatie.

Een functie schrijf je door op 1 lijn het volgende te zetten:
- Het woord `def` gevolgd door een spatie
- De naam van de functie. Die kies je zelf.
- Tussen ronden haakjes de namen (die kies je ook zelf) van de argumenten. Tussen elk argument staat een komma.
- Een dubbel punt.

De instructies van de functie komen op de volgende lijnen, telkens met 4 spaties ervoor.

Voorbeeld:

```python
def hallo(naam):
    print(f"Hallo {naam}!")

hallo("Jan")
hallo("mama")
```

## Stap 1: De figuren

Voor de figuren gaan we emojis gebruiken. Met Python kan je emojis afbeelden - probeer maar eens volgend stukje code:

```python
print("\U0001F609")
```

Op [deze pagina](https://unicode.org/emoji/charts/full-emoji-list.html) vind je alle emojis terug. Voor het voorbeeld hierboven gebruiken we "winking face" ("gezicht met knipoog" in het Engels). In de tweede kolom vinden we de juiste code: `U+1F609`. Om die te gebruiken in Python moet er een `\` symbool voor komen, en wordt de `+` vervangen door nullen tot we in het totaal 8 karakters hebben (na de `\U`).

Kies alvast je favorieten uit om in het spel te gebruiken!

Als we 4 rijen van 6 kaartjes willen en elke emoji op 2 kaartjes zal staan, dan hebben we dus 4*6/2 = 12 verschillende emojis nodig. Die zetten we best in een lijst. Als je nog niet hebt gekozen kan je alvast met de volgende lijst beginnen. We zetten er telkens de engelstalige naam bij als comentaar zodat we later nog weten wat elke code betekent.

```python
symbolen = [
    "\U0001F609", # winking face
    "\U0001F922", # nauseated face
    "\U0001F636", # face without mouth
    "\U0001F913", # nerd face
    "\U0001F971", # yawning face
    "\U0001F61B", # face with tongue
    "\U0001F631", # face screaming in fear
    "\U0001F633", # flushed face
    "\U0001F60E", # smiling face with sunglasses
    "\U0001F973", # partying face
    "\U0001F976", # cold face
    "\U0001F975", # hot face
]
```

Die lijst bevat elke emoji 1 keer. Maar we hebben elke emoji 2 keer nodig. De lijst zou eigenlijk ook in een willekeurige volgorde moeten staan.

```python
# lijst uitbreiden met zichzelf:
symbolen.extend(symbolen)

# lijst in willekeurige volgorde zetten
random.shuffle(symbolen)

# test: hoe zie de lijst er nu uit?
print(symbolen)
```

## Stap 2: Speelveld

Om het speelveld af te beelden en de speler figuren laten aanklikken gaan we [`tkinter`](https://docs.python.org/3/library/tkinter.html) gebruiken. Deze module is niet zo eenvoudig en je kan er allerlei grafische applicaties mee bouwen.

We gaan stap voor stap te werk. Probeer onderstaande code uit te voeren. Als het goed is krijg je een venster met de naam "memory", met daarin twee grote knoppen. Je kan op de knoppen klikken, maar er gebeurd nog niks.

```python
from tkinter import Tk, Button

# Eerst maken we een basis venster voor onze hele applicatie
venster = Tk()

# Hiermee stellen we de titel in die bovenaan het venster te zien zal zijn
venster.title("memory")

# Hiermee zorgen we dat zowel de breedte (width) and de hoogte (height) van het venster
# niet kunnen worden aangepast (resize)
venster.resizable(width=False, height=False)

# We maken een knop (Button) in het hoofdvenster (venster) met een bepaalde breedte en hoogte
# Daarna plaatsen die knop in een rooster in dat venster, in de kolom 0 en rij 0 (links bovenaan dus)
knop1 = Button(venster, width=5, height=5)
knop1.grid(column=0, row=0)

# Hier doe we hetzelfde met een tweede knop. Die komt in kolom 1.
knop2 = Button(venster, width=5, height=5)
knop2.grid(column=1, row=0)

# Hiermee starten we het programma
venster.mainloop()
```

We hebben natuurlijk een groter speelveld nodig. Probeer de code hierboven aan te passen zodat we een veld krijgen met 4 rijen van telkens 6 knoppen. Maak gebruik van lussen zodat je niet de code voor elke knop moet herhalen.

Tip: een lus waarbij de variable `x` de waardes 0 tot 3 zal hebben kan je zo maken:

```python
for x in range(4):
    print(f{x is {x}})
```

Als het good is krijgen we nu een speelveld dat er zo uit ziet:

|       |       |       |       |       |       |
| ----- | ----- | ----- | ----- | ----- | ----- |
| (0,0) | (0,1) | (0,2) | (0,3) | (0,4) | (0,5) |
| (1,0) | (1,1) | (1,2) | (1,3) | (1,4) | (1,5) |
| (2,0) | (0,1) | (0,2) | (0,3) | (0,4) | (0,5) |
| (3,0) | (0,1) | (0,2) | (0,3) | (0,4) | (0,5) |

## Stap 3: Knoppen met emojis en acties

We kunnen op een knop tekst zetten. Of in de plaats van tekst, een emoji!

Dit doe je door aan `Button` een argument `text="de tekst die op de knop komt"` toe te voegen.

Probeer een van de knoppen in je code aan te passen op deze manier:

```python
# Toon een emoji op de knop
knop = Button(venster, width=5, height=5, text="\U0001F609")
```

Om iets te laten gebeuren wanneer er op een knop wordt geklikt moeten we een _functie_ als argument meegeven als we een knop (`Button`) maken. Die functie moeten we dan natuurlijk ook schrijven.

We kunnen die functie gebruiken om de tekst van de knop de veranderen!

Voeg onderstaande code toe en kijk wat er gebeurd.

```python
from tkinter import Tk, Button, messagebox

# Deze functie gaan we aan de knop meegeven
def klik_op_de_knop():
    messagebox.showinfo("Hallo", "Goed geklikt!")

# Als op knop1 wordt geklikt dan voeren we functie klik_op_de_knop uit
knop1 = Button(venster, command=klik_op_de_knop, width=5, height=5)
```

## Stap 4: Speelveld met emojis

We vertrekken van het speelveld van stap 2 en de random lijst met emojis van stap 1.

We moeten deze stappen nu samenvoegen en voor elke knop onthouden welke emoji er bij hoort. Voor elke `x, y` positie moeten we kunnen opzoeken welke knop (`Button`) op die positie staat, en welke emoji er bij hoort.

Hiervoor gaan we een "dictionary" gebruiken. Een dictionary in Python is als een speciale verzameling van dingen, net als een woordenboek. Stel je voor dat je een woordenboek hebt waarin je woorden en hun betekenissen kunt opzoeken. In een Python-dictionary kun je ook dingen opzoeken.

Stel je voor dat we een dictionary willen maken om de leeftijden van verschillende kinderen op te slaan. We kunnen de namen van de personen gebruiken als "woorden" en hun leeftijden als "betekenissen".

```python
leeftijden = {
    "Jan": 12,
    "Sarah:" 10,
    "Hakim": 13
}

# Om de leeftijd van Sarah op te zoeken gebruik je leeftijden['Sarah']
print(f"Sarah is {leeftijden['Sarah']} jaar.")
```

In plaats van namen kunnen we de `x` and `y` posities van de knoppen gebruiken om iets op te zoeken en in plaats van leeftijden kunnen we de juist knop (`Button`) en emoji opslaan.

Bvb,

```python
# Eerste maken we een lege dictionary
knoppen = {}

# Dan slaan we enkele knoppen op
knoppen[0, 0] = Button(venster, width=5, height=5, text=f"knop ({0}, {0})")
knoppen[0, 1] = Button(venster, width=5, height=5, text=f"knop ({0}, {0})")
knoppen[0, 2] = Button(venster, width=5, height=5, text=f"knop ({0}, {0})")

# Voor de emojis doen we hetzelf. Met de pop() functie halen we een emoji van onze lijst
knop_symbolen = {}
knop_symbolen[0, 0] = symbolen.pop()
knop_symbolen[0, 1] = symbolen.pop()
knop_symbolen[0, 2] = symbolen.pop()
```

Gebruik bovenstaan voorbeeld om in de dubbele for-lus uit stap 2 beide dictionaries automatisch in de vullen met knoppen en emojis.

We zien nog geen echt verschil als we het programma uitvoeren. Hiervoor zien nog een paar extra stappen nodig.

## Stap 5: Op welke knop is er geklikt?

We weten al hoe we een functie kunnen uitvoeren als er op een knop wordt geklikt. Maar we moeten natuurlijk weten op _welke_ knop er is geklikt, zodat we de juiste emoji kunnen laten zien.

Eerst voegen we de code uit stap 3 toe aan de code uit stap 4.

We willen uiteindelijk de juiste `x` en `y` positie van de knop kennen als de `klik_op_de_knop` functie wordt uitgevoerd. Hiervoor moeten we eerste argumenten toevoegen aan de functie:

```python
def klik_op_de_knop(x, y):
    # Dit is de knop (Button) waar op geklikt is
    knop = knoppen[x, y]

    # Dit is de emoji die bij deze knop hoort
    emoji = knop_symbolen[x, y]

    # Nu veranderen we de text van die knop met de emoji
    knop["text"] = emoji
```

Op het moment dat we de knoppen aanmaken (in de dubbele `for`-lus) moeten we de code ook aanpassen zodat de juiste `x` en `y` waarden worden doorgegeven aan de functie. Hiervoor hebben we een ingewikkeld stukje code nodig. We passen tegelijk de code aan zodat er eerst geen tekst in de knop staat:

```python
    knop = Button(venster, width=5, height=5, command=lambda x=x, y=y: klik_op_de_knop(x, y))
```

Als het goed is krijgen we nu ons speelveld met lege knoppen. Als we op een knop klikken verschijnt de juiste emoji.

## Stap 6: Twee geklikte knoppen vergelijken

We vertrekken van de onze code uit stap 5. Nadat een knop is geklikt blijft de emoji nu altijd staan. We moeten er voor zorgen dat dit enkel gebeurt als 2 dezelfde emojis na elkaar zijn aangeklikt! Als dat niet het geval is moeten ze terug verdwijnen.

In onze `klik_op_de_knop` functie moet we dus een aantal extra zaken te weten komen:
* Is het de eerste of the tweede knop die is klikt?
* Als het de tweede knop is, wat was dan de eerste knop?

Dit kunnen we doen met behulp van 1 extra variable, bvb `eerste_knop`, waarin we de eerste knop in opslaan. Als we starten is er natuurlijk nog geen eerste knop aangeklikt, dus we geven onze variable om te beginnen de waarde `None` (= "Geen" in het engels). Dit doen we op dezelfde plaats waar we al een aantal andere variabelen aanmaken, zoals `knoppen` en `knop_symbolen`.

```python
eerste_knop = None
knoppen = {}
knop_symbolen = {}
```

In het begin van onze `klik_op_de_knop` functie moeten we nu deze zelfde variable "ophalen". Dat doen we zo:

```python
def klik_op_de_knop(x, y):
    global eerste_knop
```

Daarna komt de code die we al hebben om de juiste emoji in de aangeklikte knop te zetten. Om ervoor te zorgen dat die emoji direct getoont wordt moeten we de knop eerste "updaten":

```python
    knop.update()
```

Wat moet er nu precies gebeuren? We hebben code nodig voor het volgende "algoritme" (dat is zoals een recept, maar dan om een computerprobleem op te lossen):

* ALS (`if`) de geklikte knop de tweede knop na elkaar is (= als we weten wat de eerste knop was)
* DAN
  * ALS (`if`) emoji (`text`) van de geklikt knop != emoji van de eerste knop
  * DAN
    * wacht even (bvb 1 seconde)
    * verberg de emojis van beide knoppen terug
  * "vergeet" de eerste knop terug (`eerste_knop = None`)
* ANDERS (`else`)
  * maak de eerste knop = de geklikte knop (`eerste_knop = knop`)

Probeer dit algoritme zelf in Python code om te zetten. Om 1 seconde te wachten kan je volgende code gebruiken:

```python
# Importeer de "time" module bovenaan het programma
import time

# Op de plaats waar je wil wachten (sleep = slaap):
            time.sleep(1)
```

# Step 7: De laatste bugs

Ons programma werkt nu al, maar er zitten nog een paar kleine bugs in. Die gaan we nu fixen! Probeer op voorhand eens of je de bugs kan laten gebeuren.

1. Als je twee keer op dezelfde knop klikt denkt ons programma dat je twee knoppen juist hebt en blijft de emoji op de knop zichtbaar. We hebben dus een extra check nodig zeker te zijn dat de eerste knop en de geklikte knop verschillende zijn! (`if eerste_knop != knop`:). Als dat niet het geval is dan moet er helemaal niets gebeuren.

2. Knopppen/emojis die al juist zijn geraden kan je nog steeds aanklikken. Hierdoor raakt ons programma helemaal in de war! We moeten er dus voor zorgen dat juist geraden knoppen de `klik_op_de_knop` functie niet meer zullen uitvoeren. Dit kan je doen door `command` in de knop te vervangen door `DISABLED` (= "uitgeschakeld" in het engels)

```python
# "DISABLED" moete we eerste uit de tkinter module importeren
from tkinter import Tk, Button, DISABLED

# Dan kunnen we, op de jusite plaats in ons programma, command van de twee juiste knoppen aanpassen
                eerste_knop["command"] = DISABLED
                knop["command"] = DISABLED
```

## Todo / uitbreidingen

* Score speler1 speler2

* Resizable:

```
# https://stackoverflow.com/a/7591453
venster = Tk()
frame = Frame(venster)
venster.rowconfigure(0, weight=1)
venster.columnconfigure(0, weight=1)
frame.grid(row=0, column=0, sticky="news")
grid = Frame(frame)
grid.grid(sticky="news", column=0, row=7, columnspan=2)
frame.rowconfigure(7, weight=1)
frame.columnconfigure(0, weight=1)

#example values
for x in range(10):
    for y in range(5):
        btn = Button(frame)
        btn.grid(column=x, row=y, sticky="news")

frame.columnconfigure(tuple(range(10)), weight=1)
frame.rowconfigure(tuple(range(5)), weight=1)

venster.mainloop()
```
