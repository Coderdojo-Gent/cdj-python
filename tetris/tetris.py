"""Tetris."""

import random

import pygame

KOLOMMEN = 10
RIJEN = 20
CELL_GROOTTE = 40
BLOK_OFFSET = pygame.Vector2(KOLOMMEN // 2, -1)

SPEELVELD_BREEDTE = KOLOMMEN * CELL_GROOTTE
SPEELVELD_HOOGTE = RIJEN * CELL_GROOTTE

RAND_BREEDTE = 20

VENSTER_HOOGTE = SPEELVELD_HOOGTE + 2 * RAND_BREEDTE
VENSTER_BREEDTE = SPEELVELD_BREEDTE + 2 * RAND_BREEDTE

GEEL = "#F1E60D"
ROOD = "#E51B20"
BLAUW = "#204B9B"
GROEN = "#65B32E"
PAARS = "#7B217F"
ORANJE = "#F07E13"
GRIJS = "#1C1C1C"
WIT = "#FFFFFF"

TETROMINOS = {
    "T": {"blok_posities": [(0, 0), (-1, 0), (1, 0), (0, -1)], "kleur": "purple"},
    "O": {"blok_posities": [(0, 0), (0, -1), (1, 0), (1, -1)], "kleur": "yellow"},
    "J": {"blok_posities": [(0, 0), (0, -1), (0, 1), (-1, 1)], "kleur": "blue"},
    "L": {"blok_posities": [(0, 0), (0, -1), (0, 1), (1, 1)], "kleur": "orange"},
    "I": {"blok_posities": [(0, 0), (0, -1), (0, -2), (0, 1)], "kleur": "cyan"},
    "S": {"blok_posities": [(0, 0), (-1, 0), (0, -1), (1, -1)], "kleur": "green"},
    "Z": {"blok_posities": [(0, 0), (1, 0), (0, -1), (-1, -1)], "kleur": "red"},
}


class Blok(pygame.sprite.Sprite):
    def __init__(self, group, kleur, positie):
        """positie is (x, y) bvb (2, 3)"""
        super().__init__(group)
        self.positie = pygame.Vector2(positie) + BLOK_OFFSET
        self.image = pygame.Surface((CELL_GROOTTE, CELL_GROOTTE))
        self.image.fill(kleur)

        self.rect = self.image.get_rect(topleft=self.positie * CELL_GROOTTE)

    def update(self):
        self.rect.topleft = self.positie * CELL_GROOTTE


class Tetromino:
    def __init__(self, group, vorm, speelveld_blokken):
        self.speelveld_blokken = speelveld_blokken
        self.blokken: list[Blok] = []
        for positie in TETROMINOS[vorm]["blok_posities"]:
            self.blokken.append(Blok(group, TETROMINOS[vorm]["kleur"], positie))

    def is_beneden(self):
        for blok in self.blokken:
            # Op laatse rij van speelveld?
            if blok.positie.y == RIJEN - 1:
                return True
            # Boven reeds geplaatst blok?
            if (
                blok.positie.y >= 0
                and self.speelveld_blokken[int(blok.positie.y + 1)][int(blok.positie.x)]
            ):
                return True
        return False

    def val(self):
        if self.is_beneden():
            return

        for blok in self.blokken:
            blok.positie.y += 1

    def verplaats(self, kolom):
        """Verplaats de Tetromino naar 'kolom' plaatsen naar links of rechts.

        Als kolom > 0 -> verplaats naar rechts
        Als kolom < 0 -> verplaats naar links
        """
        for blok in self.blokken:
            # Tegen rand links?
            if blok.positie.x == 0 and kolom < 0:
                return
            # Tegen rand rechts?
            if blok.positie.x == KOLOMMEN - 1 and kolom > 0:
                return
            # Tegen reeds geplaatst blok
            if self.speelveld_blokken[int(blok.positie.y)][int(blok.positie.x + kolom)]:
                return
        for blok in self.blokken:
            blok.positie.x += kolom


pygame.init()
pygame.display.set_caption("Tetris!")
venster = pygame.display.set_mode((VENSTER_BREEDTE, VENSTER_HOOGTE))
speelveld = pygame.Surface((SPEELVELD_BREEDTE, SPEELVELD_HOOGTE))
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

val_snelheid = 1000  # miliseconden
val_tijd = 1000
beweeg_snelheid = 100
beweeg_tijd = 1000

speelveld_blokken = []
for r in range(RIJEN):
    speelveld_blokken.append([])
    for k in range(KOLOMMEN):
        speelveld_blokken[r].append(0)
for r in speelveld_blokken:
    print(r)

# Tetromino
tetromino = Tetromino(
    sprites, random.choice(list(TETROMINOS.keys())), speelveld_blokken
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    tijd = pygame.time.get_ticks()

    if tijd >= beweeg_tijd or tetromino.is_beneden():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            tetromino.verplaats(-1)
            beweeg_tijd = tijd + beweeg_snelheid
        if keys[pygame.K_RIGHT]:
            tetromino.verplaats(1)
            beweeg_tijd = tijd + beweeg_snelheid
        if keys[pygame.K_DOWN]:
            tetromino.val()
            beweeg_tijd = tijd + beweeg_snelheid
            val_tijd = tijd + val_snelheid

    if tetromino.is_beneden():
        for blok in tetromino.blokken:
            speelveld_blokken[int(blok.positie.y)][int(blok.positie.x)] = blok
        for r in speelveld_blokken:
            print(r)

        # Afgewerkte volle rijen weg doen
        volle_rijen = []
        for rij, blokken in enumerate(speelveld_blokken):
            # Op elke positie in deze rij staat een blok (geen nullen)
            if all(blokken):
                volle_rijen.append(rij)

                # Blok sprites op deze rij vernietigen
                for kolom, blok in enumerate(blokken):
                    blok.kill()

        if volle_rijen:
            # speelveld_blokken opnieuw bouwen, eerste alles nul
            speelveld_blokken = []
            for r in range(RIJEN):
                speelveld_blokken.append([])
                for k in range(KOLOMMEN):
                    speelveld_blokken[r].append(0)

            # Voor elke blok die nog bestaat:
            # - 1 rij naar beneden zaken
            # - toevoegen in speelveld_blokken
            for blok in sprites:
                blok.positie.y += 1
                speelveld_blokken[int(blok.positie.y)][int(blok.positie.x)] = blok

        # Nieuwe random tetromino bovenaan
        tetromino = Tetromino(
            sprites, random.choice(list(TETROMINOS.keys())), speelveld_blokken
        )

    speelveld.fill(GRIJS)

    if tijd >= val_tijd:
        val_tijd = tijd + val_snelheid
        tetromino.val()

    sprites.update()
    sprites.draw(speelveld)

    # ROOSTER
    for kolom in range(1, KOLOMMEN):
        x = kolom * CELL_GROOTTE
        pygame.draw.line(speelveld, WIT, (x, 0), (x, SPEELVELD_HOOGTE), 2)
    for rij in range(1, RIJEN):
        y = rij * CELL_GROOTTE
        pygame.draw.line(speelveld, WIT, (0, y), (SPEELVELD_BREEDTE, y), 2)
    pygame.draw.rect(speelveld, WIT, (0, 0, SPEELVELD_BREEDTE, SPEELVELD_HOOGTE), 2)

    venster.blit(speelveld, (RAND_BREEDTE, RAND_BREEDTE))
    pygame.display.update()
    clock.tick()
    clock.tick()
