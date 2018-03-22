import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

# Font Settings
pygame.font.init()
FONT = pygame.font.Font(None, 15)

# Color Settings
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Screen Settings
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT

# Initializing Screen
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Template')

# FUNCTIONS-----------------------------------------------------------------------------FUNCTIONS


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# MAIN LOOP--------------------------------------------------------------------------------MAIN


while True:
    event_handler()

    pygame.display.update()
    DS.fill([0, 0, 0])
