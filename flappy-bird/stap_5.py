"""Flappy Bird - Stap 5"""

import pygame

ACHTERGROND = pygame.image.load("afbeeldingen/achtergrond.png")
GROND = pygame.image.load("afbeeldingen/grond.png")

VENSTER_BREEDTE = ACHTERGROND.get_width()
VENSTER_HOOGTE = ACHTERGROND.get_height() + GROND.get_height()


class Vogel(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("afbeeldingen/vogel-midden.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.snelheid = 0

    def update(self, vlieg_omhoog=False):
        if vlieg_omhoog:
            self.snelheid = -10
        else:
            self.snelheid += 0.5
            self.rect.y += int(self.snelheid)


class Buis(pygame.sprite.Sprite):

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


pygame.init()

venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))

vogel = Vogel(100, VENSTER_HOOGTE // 2)
vogel_groep = pygame.sprite.Group()
vogel_groep.add(vogel)

buis_onder = Buis(300, VENSTER_HOOGTE // 2)
buis_boven = Buis(300, VENSTER_HOOGTE // 2 - 150, flip=True)
buis_groep = pygame.sprite.Group()
buis_groep.add(buis_onder)
buis_groep.add(buis_boven)

klok = pygame.time.Clock()
grond_x = 0


while True:
    klok.tick(60)

    # Stop het programma als de speler op het kruisje klikt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vogel_groep.update(vlieg_omhoog=True)

    grond_x -= 5
    if grond_x + GROND.get_width() <= VENSTER_BREEDTE:
        grond_x = 0

    venster.blit(ACHTERGROND, (0, 0))

    vogel_groep.update()
    vogel_groep.draw(venster)

    buis_groep.update()
    buis_groep.draw(venster)

    venster.blit(GROND, (grond_x, ACHTERGROND.get_height()))

    pygame.display.update()
