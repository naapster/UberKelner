import pygame
import sys
from scripts.__init__ import *

class Dinning_table(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #set image

        self.image = pygame.image.load("images/dinner_table.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




