# WIP Memory

* Level: 3 - Vergevorderd
* Onderwerpen: functies

In deze opdracht maken we een eenvoudige versie van het spelletje Memory. Hierbij moeten de spelers om beurt proberen 2 "kaartjes" met dezelfde afbeelding om te draaien.

## De Spelregels

(meer info: https://nl.wikipedia.org/wiki/Memory_(spel))

* Het spel wordt gespeeld met 2 spelers
* Het speelvlak bestaat uit een 4 rijen van telkens 6 kaarten
* Elke kaart het langs een kant een figuur
* Elk figuur komt op precies 2 kaarten voor
* Bij de start van het spel zijn alle kaarten gedraaid zodat de figuren niet zichtbaar zijn
* Een speler mag 2 kaarten kiezen die worden omgedraaid
  * Als de figuren hetzelfde zijn krijgt de speler een punt en mag hij nog eens spelen
  * Als de figuren verschillende zijn worden de kaarten terug omgedraaid en gaan de beurt naar de andere speler

## Stap 0: Wat is een functie?

Een _functie_ in Python is als een speciale doos waar je een aantal instructies in kunt stoppen. Je kunt deze doos een naam geven, zoals bvb. `hallo`. Telkens wanneer je die naam noemt, weet Python welke instructies erin zitten en voert het die uit.

Een functie in Python kan ook _argumenten_ accepteren. Denk aan argumenten als extra informatie die je aan de functie kunt geven, zodat deze ermee kan werken en het resultaat kan aanpassen op basis van die informatie.

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

Voor de figuren can we emojis gebruiken. Met Python kan je emojis afbeelden, probeer maar eens volgend stukje code:

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

Om iets te laten gebeuren wanneer er op een knop wordt geklikt moeten we een _functie_ meegeven als we een knop (`Button`) maken. Die functie moeten we dan natuurlijk ook schrijven.

Voeg onderstaande code toe en kijk wat er gebeurd.

```python
from tkinter import Tk, Button, messagebox

def klik_op_de_knop():
    messagebox.showinfo("Hallo", "Goed geklikt!")

knop1 = Button(root, command=klik_op_de_knop, width=5, height=5)
```

## Todo

Resizable:

```
# https://stackoverflow.com/a/7591453
root = Tk()
frame = Frame(root)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
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

root.mainloop()
```
