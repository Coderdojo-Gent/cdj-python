# Vaardigheidskaarten

Elke kaart legt 1 ding uit dat je nodig hebt om Python-projecten te maken: wat het is, een voorbeeld, waar je moet op letten, en een kleine opdracht om het zelf te proberen. Elke kaart past op 1 A4-blad.

- **Voor je aan een project begint**: kijk in de [tabel met opdrachten](../README.md#opdrachten) wat je al moet kennen.
- **Zit je vast in een project?** Neem de kaart over dat onderwerp erbij.
- **Coaches**: print de kaarten 1 keer en leg ze klaar. Zo moet je niet steeds hetzelfde opnieuw uitleggen.

## De kaarten

| Kaart | Onderwerp | PDF |
|---|---|---|
| 1 | [Tekst tonen met print()](kaarten/01-print.md) | [pdf](pdf/01-print.pdf) |
| 2 | [Variabelen](kaarten/02-variabelen.md) | [pdf](pdf/02-variabelen.pdf) |
| 3 | [Getallen en rekenen](kaarten/03-rekenen.md) | [pdf](pdf/03-rekenen.pdf) |
| 4 | [Vragen stellen met input()](kaarten/04-input.md) | [pdf](pdf/04-input.pdf) |
| 5 | [Beslissen met if, elif en else](kaarten/05-if-elif-else.md) | [pdf](pdf/05-if-elif-else.pdf) |
| 6 | [Herhalen met een for-lus](kaarten/06-for-lus.md) | [pdf](pdf/06-for-lus.pdf) |
| 7 | [Herhalen met een while-lus](kaarten/07-while-lus.md) | [pdf](pdf/07-while-lus.pdf) |
| 8 | [Werken met tekst (strings)](kaarten/08-strings.md) | [pdf](pdf/08-strings.pdf) |
| 9 | [Lijsten](kaarten/09-lijsten.md) | [pdf](pdf/09-lijsten.pdf) |
| 10 | [Dictionaries (woordenboeken)](kaarten/10-dictionaries.md) | [pdf](pdf/10-dictionaries.pdf) |
| 11 | [Functies](kaarten/11-functies.md) | [pdf](pdf/11-functies.pdf) |
| 12 | [Modules importeren](kaarten/12-modules.md) | [pdf](pdf/12-modules.pdf) |
| 13 | [Bestanden lezen](kaarten/13-bestanden.md) | [pdf](pdf/13-bestanden.pdf) |
| 14 | [Coördinaten en kleuren](kaarten/14-coordinaten-en-kleuren.md) | [pdf](pdf/14-coordinaten-en-kleuren.pdf) |
| 15 | [Tekenen met turtle](kaarten/15-turtle.md) | [pdf](pdf/15-turtle.pdf) |
| 16 | [Een spel met pygame: de game loop](kaarten/16-pygame.md) | [pdf](pdf/16-pygame.pdf) |
| 17 | [Klassen en objecten](kaarten/17-klassen.md) | [pdf](pdf/17-klassen.pdf) |
| 18 | [Foutmeldingen lezen](kaarten/18-foutmeldingen.md) | [pdf](pdf/18-foutmeldingen.pdf) |

Alles in 1 bestand om te printen: [alle-kaarten.pdf](pdf/alle-kaarten.pdf).

## Een kaart toevoegen of aanpassen

De kaarten zijn gewone Markdown-bestanden in [kaarten/](kaarten/). Tekeningen staan als SVG in [kaarten/afbeeldingen/](kaarten/afbeeldingen/).

- Een nieuwe kaart krijgt een nummer en een naam: `19-onderwerp.md`, met de titel als `# Titel` op de eerste regel.
- Hou een kaart kort genoeg voor 1 A4-blad.
- Pas ook de [tabel met opdrachten](../README.md#opdrachten) aan als een opdracht de nieuwe kaart nodig heeft.

Maak daarna de PDF's opnieuw. Je hebt Chrome, Chromium of Edge nodig:

```text
pip install markdown pygments
python maak_pdf.py
```

Vindt het script je browser niet? Geef het pad mee: `python maak_pdf.py --browser "C:/pad/naar/msedge.exe"`. Het script waarschuwt als een kaart niet meer op 1 blad past.
