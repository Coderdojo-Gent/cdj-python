# Galgje

We gaan het bekende spel "Galgje" maken, waarbij de speler letters mag gokken om zo een woord te raden.

## De Spelregels

Het programma kiest een woord uit een lijst van mogelijke woorden.

Daarna wordt het woord getoond maar elke letter is vervangen door een sterretje (`*`). Bvb als het te raden woord `galgje` is dan toont het programma `******`.

De speler mag nu telkens een letter raden.
* Als de letter in het te raden woord voorkomt dan wordt het te raden woord opnieuw geprint. Enkel de nog te raden letters blijven verborgen door een `*`. Bvb als de `g` wordt ingegeven dan wordt `g**g**` getoond. Dan mag een volgende letter worden geraden.
* Als de letter **niet** in het te raden woord voorkomt verliest de speler 1 leven. Het overblijvende aantal levens wordt geprint en een nieuwe letter mag worden geraden. De speler start met een bepaald aantal levens, bvb 15.

In plaats van een enkele letter mag de speler ook het volledige woord proberen raden.

De speler wint als hij alle letters heeft geraden of het volledige woord juist ingeeft.

De speler verliest als hij geen levens meer overheeft

## Stap 1: Letters in het woord raden

Om te beginnen kiezen we zelf een vast woord (bvb. `galgje`) en gebruiken we een oneindige lus om telkens opnieuw de speler een letter te laten kiezen. Dan kijken we of de letter wel of niet in het woord voorkomt.

Tips:
* Voor een oneindige lus gebruik je `while True:`. Tijdens het testen kan je het programma beëindigen met de combinatie `CTRL-C`.
* Om de speler een letter te laten ingeven gebruik je de function `input()`.

## Stap 2: Geraden letter op juiste plaats tonen

Nu gaan we het te tonen woord toevoegen. Dat is het woord waarin de juist geraden letters al zijn ingevuld. Bij het begin van het spel zijn dit allemaal sterretjes (`*`). Telkens een letter juist wordt geraden gaan we die letter(s) (op de juiste plaats!) tonen in plaats van `*`.

Tips:

| g | a | l | g | j | e |
| - | - | - | - | - | - |
| 0 | 1 | 2 | 3 | 4 | 5 |

* Je kan niet 1 karakter (letter) in een _string_ veranderen. Daarom is het handig als je voor het te tonen woord in plaats van een _string_ een _list_ (lijst) van karakters gebruikt. In het begin is dit dus een lijst van sterretjes.
* Gebruik een lus (bvb `for`) om elke letter van het woord te vergelijken met de gok.
* Met de functie `enumerate()` kan je een lus maken over elke letter van het woord en ook de positie van die letter in het woord.

```python
woord = "test"
for positie, letter in enumerate(woord):
    print(positie, letter)

# Resultaat:
# 0 t
# 1 e
# 2 s
# 3 t
```

## Stap 3: Spel stoppen als het juist woord is geraden

We moeten er voor zorgen dat het spel stopt wanneer het juiste woord is geraden.
1. In plaats van een letter is het volledige woord (juist) gegokt
2. Alle letters van het woord zijn geraden

Tips:
* Om te testen of alle letters zijn geraden kan je kijken of er nog een `*` is in het te tonen woord.
* Met `break` kan je een oneindige lus (`while True:`) stoppen

## Stap 4: Levens

Tot nu toe kan je eigenlijk nooit verliezen. Het spel wordt spannender als je maar een aantal keer fout kan raden. Laat de speler ook voor elke gok weten hoeveel levens hij of zij nog heeft.
