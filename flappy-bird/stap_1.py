"""Flappy Bird - Stap 1"""

import pygame

ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()

pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

while True:
    # Stop het programma als de speler op het kruisje klikt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    venster.blit(ACHTERGROND, (0, 0))
    venster.blit(GROND, (0, ACHTERGROND.get_height()))

    pygame.display.update()
