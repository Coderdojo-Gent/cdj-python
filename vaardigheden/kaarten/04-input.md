# Vragen stellen met input()

Met `input()` stelt je programma een vraag. Het programma wacht tot de speler iets typt en op Enter drukt. Het antwoord steek je in een variabele.

## Zo werkt het

```python
naam = input("Hoe heet je? ")
print("Hallo " + naam + "!")
```

Op het scherm (de speler typt `Sam`):

```text
Hoe heet je? Sam
Hallo Sam!
```

- De tekst tussen de haakjes is de vraag. Zet er een spatie achter, anders plakt het antwoord ertegen.
- Het programma staat stil tot de speler op Enter drukt.

## Het antwoord is altijd tekst

`input()` geeft **altijd tekst** terug, ook als de speler een getal typt. Wil je rekenen met het antwoord? Zet het dan eerst om met `int()` (zie kaart 3):

```python
leeftijd = int(input("Hoe oud ben je? "))
print("Volgend jaar ben je", leeftijd + 1)
```

Zonder `int()` krijg je `TypeError: can only concatenate str (not "int") to str`.

## Voorbeeld: een kleine rekenmachine

```python
getal1 = int(input("Eerste getal: "))
getal2 = int(input("Tweede getal: "))
print("Samen is dat", getal1 + getal2)
```

## Het antwoord opkuisen

```python
antwoord = input("Wil je verder spelen? ").strip().lower()
if antwoord == "ja":
    print("Daar gaan we!")
```

- `.lower()` maakt alles klein. Zo is `"Ja"`, `"JA"` en `"ja"` allemaal hetzelfde.
- `.strip()` haalt spaties voor en achter weg.

## Let op

- Typt de speler iets dat geen getal is (bv. `tien`) terwijl je `int()` gebruikt? Dan stopt het programma met een `ValueError`. Start opnieuw en typ een getal.
- `int("3.5")` werkt niet. Voor kommagetallen gebruik je `float()`.
- Een `input()` in een online editor of in VS Code typ je in de **terminal** onderaan, niet in je code.

## Probeer het zelf

Vraag de naam en het geboortejaar van de speler. Reken uit hoe oud de speler dit jaar wordt en print bv. `Hallo Sam, jij wordt dit jaar 12!`
