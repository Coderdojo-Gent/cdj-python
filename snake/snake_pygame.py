# import module(s)
import pygame
import random

# start pygame
pygame.init()

###############
## Variables ##
###############

font = pygame.font.SysFont(None, 25)

# create a window in pygame
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

game_exit = False
game_over = False

coordX = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
coordY = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0

clock = pygame.time.Clock()

richting = None

randAppelX = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
randAppelY = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0

snakeList = []
snakeLength = 1

keylist = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

############
## Colors ##
############
achtergrond = (10, 10, 255)
zwart = (0, 0, 0)
rood = (255, 0, 0)
wit = (255, 255, 255)

###############
## Functions ##
###############


def bericht_op_scherm(bericht, kleur):
    tekst = font.render(bericht, True, kleur)
    tekst_rect = tekst.get_rect()
    tekst_rect.center = screen_width / 2, screen_height / 2
    screen.blit(tekst, tekst_rect)


def snake(snakeList):
    for XnY in snakeList:
        pygame.draw.rect(screen, zwart, [XnY[0], XnY[1], 10, 10])


def wait_for_move():
    move = False
    while not move:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in keylist:
                    richting = event.key
                    move = True


################
## While loop ##
################

counter = 0
while not game_exit:  # not false is true
    for event in pygame.event.get():
        print(event)
        if (
            event.type == pygame.QUIT
        ):  # event type "256" is pressing on the cross to close the window
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                richting = keylist[0]
            elif event.key == pygame.K_RIGHT:
                richting = keylist[1]
            elif event.key == pygame.K_UP:
                richting = keylist[2]
            elif event.key == pygame.K_DOWN:
                richting = keylist[3]

    if richting == keylist[0]:
        coordX -= 10
    elif richting == keylist[1]:
        coordX += 10
    elif richting == keylist[2]:
        coordY -= 10
    elif richting == keylist[3]:
        coordY += 10

    if (
        coordX >= screen_width - 10
        or coordX < 0
        or coordY >= screen_height - 10
        or coordY < 0
    ):
        game_over = True

    if coordX == randAppelX and coordY == randAppelY:
        randAppelX = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
        randAppelY = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
        snakeLength += 1

    screen.fill(achtergrond)
    pygame.draw.rect(screen, rood, [randAppelX, randAppelY, 10, 10])

    snakeHead = []
    snakeHead.append(coordX)
    snakeHead.append(coordY)
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]

    for eachSegment in snakeList[:-1]:
        if eachSegment == snakeHead:
            game_over = True

    snake(snakeList)

    pygame.display.update()
    clock.tick(12)

    while game_over:
        bericht_op_scherm(
            "GAME OVER! Restart the game by pressing 'R' or leave by pressing 'Q'", rood
        )
        pygame.display.update()
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # event type "256" is pressing on the cross to close the window
                game_exit = True
                game_over = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_exit = True
                    game_over = False
                if event.key == pygame.K_r:
                    game_over = False
                    coordX = round(random.randrange(0, screen_width - 10) / 10) * 10
                    coordY = round(random.randrange(0, screen_height - 10) / 10) * 10
                    richting = None
                    snakeList = []
                    snakeLength = 1


pygame.quit()  # pygame venster sluiten
quit()  # python sluiten
