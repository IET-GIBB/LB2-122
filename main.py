import pygame, sys, random
from pygame.locals import *

import constants

clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((constants.WINDOWWIDTH, constants.WINDOWHEIGHT), 0, 32)
saul = pygame.image.load('assets/saul.png')


def set_up_game():
    pygame.init()


set_up_game()

player = pygame.Rect(375, 600, 50, 50)
square_counter = 0
squares = []

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

startScreen = True
gameOver = False

points = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
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

    if startScreen:
        # pygame.mixer.Sound.play(pygame.mixer.Sound("assets/better_call_saul_intro.wav"), loops=-1)
        window_surface.fill(constants.WHITE)
        pygame.display.set_caption('Better dodge Saul')
        image = pygame.transform.scale(pygame.image.load("assets/Game_Background.png"),
                                       (constants.WINDOWHEIGHT / 405 * 722, constants.WINDOWHEIGHT))
        window_surface.blit(image, (constants.WINDOWWIDTH / 2 - image.get_rect().width / 2, 0))

        pygame.draw.rect(window_surface, constants.RED, pygame.Rect(200, 600, 400, 100))

        saul_image = pygame.image.load('assets/saul_head.png')
        pygame.display.set_icon(saul_image)

        basic_font = pygame.font.SysFont(None, 48)

        text = basic_font.render('Better dodge Saul', True, constants.BLACK, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = window_surface.get_rect().centerx
        text_rect.centery = window_surface.get_rect().centery

        window_surface.blit(pygame.font.SysFont("arial", 72).render("Start", True, "WHITE"), (330, 610))

        if pygame.mouse.get_pressed(3)[0] and 200 <= pygame.mouse.get_pos()[0] <= 600 <= pygame.mouse.get_pos()[
            1] <= 800:
            startScreen = False
            gameOver = False

    if not startScreen and not gameOver:
        window_surface.fill(constants.BLACK)
        window_surface.blit(pygame.font.SysFont("arial", 24).render("Points: " + str(points), True, "WHITE"), (20, 20))
        square_counter += 1
        if square_counter >= 40:
            square_counter = 0
            squares.append(pygame.Rect(random.randint(0, constants.WINDOWWIDTH - 40),
                                       random.randint(-constants.WINDOWHEIGHT, 0), 40, 40))

        if moveUp and moveDown and moveLeft and moveRight:

        elif moveUp and moveDown and moveLeft:
            player.x -= constants.MOVESPEED

        elif moveUp and moveDown:
            player.y = player.y

        elif moveLeft and moveRight:
            player.x = player.x

        else:
            if moveUp and player.y >= 0:
                player.y -= constants.MOVESPEED
            if moveDown and player.y + 50 <= constants.WINDOWHEIGHT:
                player.y += constants.MOVESPEED
            if moveLeft and player.x >= 0:
                player.x -= constants.MOVESPEED
            if moveRight and player.x + 50 <= constants.WINDOWWIDTH:
                player.x += constants.MOVESPEED

        pygame.draw.rect(window_surface, constants.WHITE, player)

        for s in squares[:]:
            s.y += constants.SQUARESSPEED
            if player.colliderect(s):
                player.width = 0
                player.height = 0
                gameOver = True
                squares.remove(s)

            if s.y >= constants.WINDOWHEIGHT:
                squares.remove(s)
                points += 1

        for i in range(len(squares)):
            pygame.draw.rect(window_surface, constants.RED, squares[i])

    if not startScreen and gameOver:
        window_surface.fill(constants.BLACK)
        window_surface.blit(pygame.font.SysFont("arial", 84).render("Game Over", True, "White"), (230, 200))
        pygame.draw.rect(window_surface, constants.RED, pygame.Rect(200, 600, 400, 100))
        window_surface.blit(pygame.font.SysFont("arial", 72).render("Resume", True, "WHITE"), (300, 610))

        if pygame.mouse.get_pressed(3)[0] and 200 <= pygame.mouse.get_pos()[0] <= 600 <= pygame.mouse.get_pos()[
            1] <= 800:
            startScreen = True

    pygame.display.update()

    # FPS
    clock.tick(120)
