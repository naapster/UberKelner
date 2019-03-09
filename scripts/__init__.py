
# filename __init__ is required to treat scripts folder as resource

# graphics init

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# variable for size of sprites in px
blocksize = 30

# var for number of blocks in row of simulation
global N; N = 10

WINDOW_WIDTH = blocksize * N
WINDOW_HEIGHT = blocksize * N

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('UberKelner')

WHITE = (255, 255, 255)

all_sprites_list = pygame.sprite.Group()
