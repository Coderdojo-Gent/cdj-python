"""Flappy Bird - Stap 3"""

import pygame

ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()


class Vogel(pygame.sprite.Sprite):
    # __init__ is een speciale functie die een nieuw object maakt
    def __init__(self, x, y):
        # Eerste gebruiken we de __init__ functie van the Spite klasse
        pygame.sprite.Sprite.__init__(self)
        # Dan laden we de afbeelding van de vogel in
        self.image = pygame.image.load("afbeeldingen/vogel-midden.png")
        # Pygame heeft een rechthoek (rectangle) nodig om te weten waar
        # de sprite geplaatst moet worden
        self.rect = self.image.get_rect()
        # De x en y coordinaten gebruiken we om het midden van de rechthoek te bepalen
        self.rect.center = (x, y)


pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

# Maak een Vogel en plaats hem in een nieuwe sprite groep
vogel = Vogel(100, VENSTER_HOOGTE // 2)
vogel_groep = pygame.sprite.Group()
vogel_groep.add(vogel)

klok = pygame.time.Clock()
grond_x = 0

while True:
    klok.tick(60)

    # Stop het programma als de speler op het kruisje klikt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    grond_x -= 5
    if grond_x + GROND.get_width() <= VENSTER_BREEDTE:
        grond_x = 0

    venster.blit(ACHTERGROND, (0, 0))
    venster.blit(GROND, (grond_x, ACHTERGROND.get_height()))

    # Teken de vogel_groep in het venster
    vogel_groep.draw(venster)

    pygame.display.update()
