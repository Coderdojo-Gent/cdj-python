# Bestanden lezen

Je programma kan tekst uit een bestand lezen, bijvoorbeeld een lange lijst woorden. Zo hoef je niet alles zelf in je code te typen.

## Zo werkt het

Zet het bestand (bv. `woorden.txt`) in **dezelfde map** als je Python-programma.

```python
with open("woorden.txt") as bestand:
    inhoud = bestand.read()
print(inhoud)
```

- `open("woorden.txt")` opent het bestand.
- `with ... as bestand:` geeft het open bestand de naam `bestand`. Na het blok dat inspringt, sluit Python het bestand vanzelf.
- `bestand.read()` leest alles in 1 lange string.

## Regel per regel: een lijst

Met `splitlines()` knip je de tekst in stukken: elke regel wordt een element van een lijst (kaart 9).

Inhoud van `woorden.txt`:

```text
appel
banaan
kers
```

```python
with open("woorden.txt") as bestand:
    woorden = bestand.read().splitlines()
print(woorden)         # ['appel', 'banaan', 'kers']
print(len(woorden))    # 3
```

Nu kan je alles met de lijst doen wat je al kent, bv. een willekeurig woord kiezen met `random.choice(woorden)` (kaart 12).

## Schrijven naar een bestand

Met `"w"` (*write*) maak je een nieuw bestand:

```python
with open("score.txt", "w") as bestand:
    bestand.write("Hoogste score: 42")
```

Pas op: `"w"` wist alles wat al in het bestand stond. Met `"a"` (*append*) schrijf je er achteraan bij.

## Let op

- `FileNotFoundError`: Python vindt het bestand niet. Staat het in dezelfde map? Klopt de naam, ook `.txt`? Heb je in VS Code de juiste map geopend?
- Zie je rare tekens zoals `Ã«` in plaats van `ë`? Gebruik `open("woorden.txt", encoding="utf-8")`.

## Probeer het zelf

Maak een bestand `moppen.txt` met op elke regel een mop. Schrijf een programma dat een willekeurige mop print.
