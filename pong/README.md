# Pong

* Level: 3 - Vergevorderd
* Onderwerpen: pygame, lussen, constanten, wiskunde

In deze opdracht maken we een eenvoudige versie van het computerspel Pong.

## De Spelregels

https://nl.wikipedia.org/wiki/Pong

Pong is een van de eerste computerspellen uit 1972! Pong is gebaseerd op tafeltennis (of pingpong). Het spel werkt met twee paletten (of batjes), een balletje en twee muren aan de zijkant. De bedoeling van het spel is dat het balletje achter het palet van de tegenspeler terechtkomt. In dat geval wordt een punt gescoord. De score verschijnt bovenin het scherm. Er wordt een bepaalde tijd gespeeld of het er wordt gespeeld tot een speler een bepaald aantal punten,bvb 10 punten, heeft gescoord.

![](https://upload.wikimedia.org/wikipedia/commons/6/62/Pong_Game_Test2.gif)

## Stap 0: Pygame

Bekijk de [Snake opdracht](../snake/pygame%20cursus.pdf). Daar vind je een inleiding over Pygame en uitleg hoe je het moet installeren.

## Stap 1: Het Speelveld en de Pygame "event loop"

De module `pygame` moeten we bovenaan ons programma eerste "importeren".

Pygame moet je daarna ook nog eens "inladen". Dat doe je met de functie `pygame.init()`.

Om een venster te maken gebruiken we de functie `pygame.display.set_mode((breedte, hoogte))`. Voor ons spel hebben we maar 1 venster nodig. Voor de "breedte" gebruiken we 800 (pixels) en voor de hoogte 600. Zo krijgen we een rechthoekig venster. Het resultaat van die functie hebben we later nog nodig, dus we moet die opslaan in een variable. Die noemen we bvb. gewoon `venster`.

Om spellen met Pygame te maken gebruiken een `while` lus. Die lus stop pas als de variabele `stoppen` `True` wordt. Dat doen we in de lus als we zien dat de speler wil stoppen (bvb door het venster te sluiten of op een bepaalde toets te duwen).

In die `while` lust gebruiken we een tweede lus. Een `for` lus. Daarmee bekijken we alle gebeurtenissen (`event`s) die er zijn geweest. Een gebeurtenis is bvb. een toets die wordt ingedrukt of de muis die beweegt. Als we zien dat een van die gebeurtenissen `pygame.QUIT` is, dat is waneer het venster wordt gesloten, maken we de variable `stoppen` `True` zodat het programma stopt. Dit stukje code ziet er bvb zo uit:

```python
stoppen = False
while not stoppen:
    # Bekijk alle events (gebeurtenissen)
    for event in pygame.event.get():
        print(event)

        # De event "pygame.QUIT" krijgen we als het venster wordt gesloten
        if event.type == pygame.QUIT:
            stoppen = True
```

We willen ons speelveld (= het volledige venster) ook helemaal zwart maken. Dat doen we met de functie `venster.fill((0, 0, 0))`. Die functie moet ook in dezelfde `while` lus komen. Daarna moeten we Pygame ook nog de instructie geven om alle verandering (tot nu toe is dat enkel het vullen van het venster met een kleur) bij te werken. Dat doen we met de functie `pygame.display.update()`.

`(0, 0, 0)` is de _RGB kleurcode_ voor zwart. Op de website https://www.google.com/search?q=google+color+picker kan je kleuren kiezen en de RGB code aflezen. Als je wil kan je ook een ander kleur dan zwart proberen.

## Step 2: Constanten en het balletje

## Stap 3: Bal laten bewegen en botsen

