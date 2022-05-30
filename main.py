import pygame, sys
from pygame.locals import *

import constants


def set_up_game():
    pygame.init()

    window_surface = pygame.display.set_mode((constants.WINDOWWIDTH, constants.WINDOWHEIGHT), 0, 32)
    window_surface.fill(constants.WHITE)
    pygame.display.set_caption('Better dodge Saul')
    image = pygame.transform.scale(pygame.image.load("assets/Game_Background.png"), (constants.WINDOWHEIGHT / 405 * 722, constants.WINDOWHEIGHT))
    window_surface.blit(image, (constants.WINDOWWIDTH / 2 - image.get_rect().width / 2, 0))
    saul_image = pygame.image.load('assets/saul_head.png')

    pygame.display.set_icon(saul_image)

    basic_font = pygame.font.SysFont(None, 48)

    text = basic_font.render('Better dodge Saul', True, constants.BLACK, constants.WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = window_surface.get_rect().centerx
    text_rect.centery = window_surface.get_rect().centery

    # pygame.draw.rect(window_surface, constants.RED, (text_rect.left - 20,
    #                                                  text_rect.top - 20,
    #                                                  text_rect.width + 40,
    #                                                  text_rect.height + 40))



set_up_game()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
