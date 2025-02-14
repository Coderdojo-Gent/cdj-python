"""Flappy Bird - Stap 2"""

import pygame

ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()

pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
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

    pygame.display.update()
