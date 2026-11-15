# Tekst tonen met print()

Met `print()` zet je iets op het scherm. Het is de eerste instructie die bijna elke programmeur leert.

## Zo werkt het

```python
print("Hallo CoderDojo!")
```

Op het scherm: `Hallo CoderDojo!`

- Tekst zet je tussen aanhalingstekens: `"zo"` of `'zo'`. Tekst heet in Python een *string*.
- Getallen hoeven niet tussen aanhalingstekens. Python rekent ze zelfs uit.
- Wil je meerdere dingen tonen? Zet er een komma tussen. Python zet dan zelf een spatie.
- Een lege `print()` geeft een lege regel.

## Voorbeelden

| Code | Op het scherm |
|---|---|
| `print("3 + 4")` | `3 + 4` |
| `print(3 + 4)` | `7` |
| `print("Ik ben", 12, "jaar")` | `Ik ben 12 jaar` |
| `print("Hallo " + "Jan")` | `Hallo Jan` |
| `print("Hallo" + "Jan")` | `HalloJan` (met `+` zet Python geen spatie) |
| `print("Eerste regel\nTweede regel")` | `\n` begint een nieuwe regel |

## Een programma met meerdere regels

Python voert je programma uit van boven naar onder, regel per regel:

```python
print("Welkom bij het raadspel!")
print("Raad een getal tussen 1 en 10.")
print()
print("  /\\_/\\")
print(" ( o.o )")
print("  > ^ <")
```

Op het scherm:

```text
Welkom bij het raadspel!
Raad een getal tussen 1 en 10.

  /\_/\
 ( o.o )
  > ^ <
```

Een `\` is een speciaal teken in een string. Wil je echt een `\` zien, schrijf er dan 2: `\\`.

## Let op

- Elk aanhalingsteken dat je opent, moet je ook sluiten. `print("Hallo)` geeft een `SyntaxError`.
- Schrijf `print` met een kleine letter. `Print("Hallo")` werkt niet.
- Vergeet de haakjes niet: `print "Hallo"` werkt niet in Python 3.
- Gebruik gewone aanhalingstekens `"`. Gekrulde aanhalingstekens `“ ”` (uit Word of een PDF) werken niet.

## Probeer het zelf

1. Print je naam en je leeftijd op 1 regel.
2. Teken een figuurtje (een huis, een raket, een gezicht) met een paar `print()`-regels.
