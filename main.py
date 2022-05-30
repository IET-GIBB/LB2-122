import pygame, sys, random
from pygame.locals import *

import constants

clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((constants.WINDOWWIDTH, constants.WINDOWHEIGHT), 0, 32)
saul = pygame.image.load('assets/saul.png')


def set_up_game():
    pygame.init()
    saul_image = pygame.image.load('assets/saul_head.png')
    pygame.display.set_icon(saul_image)
    pygame.display.set_caption('Better Dodge Saul')
    window_surface.fill(constants.BLACK)


set_up_game()

player = pygame.Rect(300, 100, 50, 50)

square_counter = 0
squares = []
for i in range(10):
    squares.append(pygame.Rect(random.randint(0, constants.WINDOWWIDTH - 40),
                                   random.randint(0, constants.WINDOWHEIGHT - 40), 40, 40))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, constants.WINDOWHEIGHT - player.height)
                player.left = random.randint(0, constants.WINDOWWIDTH - player.width)

    window_surface.fill(constants.BLACK)

    square_counter += 1
    if square_counter >= 40:
        square_counter = 0
        squares.append(pygame.Rect(random.randint(0, constants.WINDOWWIDTH - 40),
                                   random.randint(0, constants.WINDOWHEIGHT - 40), 40, 40))

    if moveDown and player.bottom < constants.WINDOWHEIGHT:
        player.top += constants.MOVESPEED
    if moveUp and player.top > 0:
        player.top -= constants.MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= constants.MOVESPEED
    if moveRight and player.right < constants.WINDOWWIDTH:
        player.right += constants.MOVESPEED

    pygame.draw.rect(window_surface, constants.WHITE, player)

    for s in squares[:]:
        if player.colliderect(s):
            squares.remove(s)

    for i in range(len(squares)):
        pygame.draw.rect(window_surface, constants.RED, squares[i])

    pygame.display.update()
    clock.tick(40)
