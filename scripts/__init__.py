#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from random import shuffle

# filename __init__ is required to treat scripts folder as resource

# variable for size of sprites in px
blocksize = 60

# var for number of blocks in row of simulation
global N; N = 10

# set window size
WINDOW_WIDTH = blocksize * N
WINDOW_HEIGHT = blocksize * N

# graphics init
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('UberKelner')
WHITE = (255, 255, 255)


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

def create_random_coordinates():
    # generate random positions list
    positions = range(N)
    matrix_fields = [[posX, posY] for posX in positions for posY in positions]
    shuffle(matrix_fields)
    return matrix_fields