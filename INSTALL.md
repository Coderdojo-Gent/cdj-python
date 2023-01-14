# Python Installeren

Er zijn vele manieren om Python te installeren en nog meer programma's of omgevingen om Python te schrijven en uit te voeren. Dit is de manier die we aanraden en die je terug vindt op de laptops van Coderdojo Gent.

We gebruiken de standaard installer van python.org + Visual Studio Code met de Python extensie.

## Windows

### Python

1. Ga naar https://www.python.org/downloads/windows/
1. Ga naar "Latest Python 3 Release"
1. Scroll naar beneden en klik op _Windows installer (64-bit)_. Kies er voor om het bestand op te slaan.
1. Open het gedownloade `.exe` bestand.
1. **Vink zeker "Add Python 3.X to PATH" aan** (bij nieuwere versies kan er "Add python.exe to PATH" staan)
1. Klik op "Install Now" en verleen toestemming wanneer gevraagd.
1. Eenmaal geïnstalleerd, klik op "Disable path length limit", waar je ook toestemming voor moet verlenen.
1. Sluit de installer.

### Visual Studio Code

1. Ga naar https://code.visualstudio.com
1. Klik op _Download for Windows_. Kies er voor om het bestand op te slaan.
1. Open het gedownloade `.exe` bestand.
1. Aanvaard de licentie overeenkomst. Verder kan je in principe alle standaardinstellingen van de installer gebruiken.

## MacOS

### Python

1. Ga naar https://www.python.org/downloads/mac-osx/
1. Ga naar "Latest Python 3 Release".
1. Scroll naar beneden en klik op _macOS 64-bit universal2 installer_. Kies er voor om het bestand op te slaan.
1. Open het gedownloade bestand en volg de instructies.

### Visual Studio Code

1. Ga naar https://code.visualstudio.com
1. Klik op _Download for MAc_. Kies er voor om het bestand op te slaan.
1. Open het gedownloade `.zip` bestand.
1. Sleep de applicatie in het bestand naar je Applications map.

## Visual Studio Code Python extensie

Deze extensie maakt het een stuk eenvoudiger om Python code te schrijven en uit te voeren in VS Code.

1. Start Visual Studio Code als dat nog niet gebeurd is.
1. Klik in de linker balk op het icoon met 4 vierkantjes.
1. Zoek naar _Python_.
1. Klik op de extensie bovenaan de lijst. Er staat _Microsoft_ bij.
1. Klik op Install.

## Installatie testen

1. Start Visual Studio Code.
1. Klik in de linker balk op het bovenste icoon met 2 documenten. Klik dan op _Open Folder_.
1. Kies een bestaande map (= folder), of maak een nieuwe aan, waar je je Python programmas wil bewaren.
1. Met een rechter muisklik binnen het hoofdscherm kies je voor _New Text File_.
1. Tik het volgende in het nieuwe bestand: `print("CoderDojo Gent!")`.
1. Sla het bestand op (`CTRL-s` of `CMD-s` op een Mac). Geef het bestand de naam `test.py`.
1. Door het `.py` extensie weet VS Code nu dat het om een Python bestand gaat. De tekst is nu gekleurd . Rechts bovenaan staat er nu ook een _Play_ knop (driehoekje naar rechts). Door op die knop te klikken kan je het programma uitvoeren.
1. Klik op de play knop om het programma uit te voeren. Er verschijnt een nieuw "terminal" venster onderaan. Daarin wordt automatisch het programma uitgevoerd. Dat zou er ongeveer zo moeten uit zien:

```
PS C:\Users\gebruiker\coderdojo> C:/Users/gebruiker/AppData/Local/Programs/Python/Python311/python.exe c:/Users/gebruiker/coderdojo/test.py
CoderDojo Gent!
```
