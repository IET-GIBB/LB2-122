import pygame, sys
from pygame.locals import *

import colors


def set_up_game():
    pygame.init()

    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Hello world!')

    basicFont = pygame.font.SysFont(None, 48)

    text = basicFont.render('Better dodge Saul', True, colors.BLACK, colors.WHITE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery

    pygame.draw.rect(windowSurface, colors.RED, (textRect.left - 20,
                                                 textRect.top - 20,
                                                 textRect.width + 40,
                                                 textRect.height + 40))

    windowSurface.fill(colors.WHITE)

    pygame.display.update()


set_up_game()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
