#!/usr/bin/python
# -*- coding: utf-8 -*-

# legacy init script with global variables:

import pygame


# filename __init__ is required to treat scripts folder as resource

# variables:

# size of sprites in px
blocksize = 60

# number of blocks in row of simulation
N = 6


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



