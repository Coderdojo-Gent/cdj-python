"""Flappy Bird - Stap 10"""

import itertools
import random
import pygame

# Achtergrond and grond afbeeldingen inladen
ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()


class Vogel(pygame.sprite.Sprite):
    """De Vogel klasse stelt de vogel voor"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        afbeeldingen = [
            pygame.image.load("afbeeldingen/vogel-omhoog.png"),
            pygame.image.load("afbeeldingen/vogel-midden.png"),
            pygame.image.load("afbeeldingen/vogel-omlaag.png"),
        ]
        self.flapper_cycle = itertools.cycle(afbeeldingen)
        # Start met de eerste afbeelding uit afbeeldingen
        self.image = next(self.flapper_cycle)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.snelheid = 0

    def update(self, vlieg_omhoog=False, flapper=False):
        if vlieg_omhoog:
            self.snelheid = -10
        elif flapper:
            self.image = next(self.flapper_cycle)
        else:
            self.snelheid += 0.5
            self.rect.y += int(self.snelheid)


class Buis(pygame.sprite.Sprite):
    """De Buis klasse stelt 1 buis (boven of onder) voor"""

    def __init__(self, x, y, flip=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("afbeeldingen/buis.png")
        self.rect = self.image.get_rect()
        if flip:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y)
        else:
            self.rect.topleft = (x, y)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()


pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
klok = pygame.time.Clock()

vogel = Vogel(100, VENSTER_HOOGTE // 2)
vogel_groep = pygame.sprite.Group()
vogel_groep.add(vogel)

flapper_tijd = pygame.time.get_ticks()
# Flapper 10 keer per seconde
flapper_interval = 100

laatste_buis = pygame.time.get_ticks()
# Elke 1,5 seconden een nieuw paar buizen
buis_interval = 1500
buis_groep = pygame.sprite.Group()

# Om de grond de laten scrollen
grond_x = 0

# Bepaald of het spel gestart is
start = False

# Om te controleren of the vogel precies tussen de buizen zit
vliegt_door_buis = False
# Het lettertype en de kleur van de tekst voor de score te laten zien
font = pygame.font.SysFont("Bauhaus 93", 60)
wit = pygame.Color("white")
# Om te score bij te houden
score = 0


while True:
    klok.tick(60)

    # Stop het programma als de speler op het kruisje klikt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vogel_groep.update(vlieg_omhoog=True)
                # Start het spel als de spatiebalk is ingedrukt
                if not start:
                    start = True

    # Laat de grond scrollen
    grond_x -= 5
    if grond_x + GROND.get_width() <= VENSTER_BREEDTE:
        grond_x = 0
    venster.blit(GROND, (grond_x, ACHTERGROND.get_height()))

    venster.blit(ACHTERGROND, (0, 0))

    tijd = pygame.time.get_ticks()

    # Laat de vogel flapperen
    if tijd >= flapper_tijd + flapper_interval:
        vogel_groep.update(flapper=True)
        flapper_tijd = tijd

    if start:
        # Maak nieuwe buizen
        if tijd >= laatste_buis + buis_interval:
            midden = ACHTERGROND.get_height() // 2
            buis_midden = random.randrange(midden - 200, midden + 200)
            buis_onder = Buis(VENSTER_BREEDTE, buis_midden + 75)
            buis_boven = Buis(VENSTER_BREEDTE, buis_midden - 75, flip=True)
            buis_groep.add(buis_onder)
            buis_groep.add(buis_boven)
            laatste_buis = tijd

        # Score + 1 als de vogel door de buizen vliegt
        if (
            not vliegt_door_buis
            and buis_groep.has()
            and buis_groep.sprites()[0].rect.left
            < vogel_groep.sprites()[0].rect.x
            < buis_groep.sprites()[0].rect.right
        ):
            vliegt_door_buis = True
        if (
            vliegt_door_buis
            and buis_groep.has()
            and vogel_groep.sprites()[0].rect.x > buis_groep.sprites()[0].rect.right
        ):
            vliegt_door_buis = False
            score += 1

        vogel_groep.update()
        buis_groep.update()

    # Teken de vogel, buizen en score
    vogel_groep.draw(venster)
    buis_groep.draw(venster)
    venster.blit(
        font.render(str(score), True, wit),
        (int(VENSTER_BREEDTE // 2), 20),
    )

    # Game over als de vogel een van de buizen raakt
    if (
        pygame.sprite.groupcollide(vogel_groep, buis_groep, False, False)
        or vogel.rect.top < 0
        or vogel.rect.bottom > ACHTERGROND.get_height()
    ):
        buis_groep.empty()
        vogel.rect.x = 100
        vogel.rect.y = VENSTER_HOOGTE // 2
        start = False
        score = 0

    pygame.display.update()
