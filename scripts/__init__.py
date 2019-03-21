#!/usr/bin/python
# -*- coding: utf-8 -*-

# legacy init script with global variables:

import pygame
from random import shuffle

# filename __init__ is required to treat scripts folder as resource

# variables:

# size of sprites in px
blocksize = 60

# number of blocks in row of simulation
global N
N = 10

# frames per second setting
FPS = 30

# window size
WINDOW_WIDTH = blocksize * N
WINDOW_HEIGHT = blocksize * N

# graphics init
pygame.init()
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('UberKelner')
WHITE = (255, 255, 255)


# init sprite sprite_name on coordinate x, y
def init_graphics(self, x, y, sprite_name):
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # init graphics - do not touch!
    pygame.sprite.Sprite.__init__(self)
    # set image
    self.image = pygame.image.load("images/" + sprite_name + ".png")
    # resize image to blocksize
    self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
    # set coordinates
    self.rect = self.image.get_rect()
    self.rect.x = x * blocksize
    self.rect.y = y * blocksize
    # //////////////////////////////////////////////////


# generate random positions list for all objects
def create_random_coordinates():
    # list of all possible numbers of coordinate
    positions = range(N)
    # cartesian product of all possible numbers
    matrix_fields = [[posX, posY] for posX in positions for posY in positions]
    # randomize order of coordinates
    shuffle(matrix_fields)
    return matrix_fields