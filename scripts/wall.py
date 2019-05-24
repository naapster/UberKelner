# furnace object class:

import pygame
from UberKelner import init_graphics


# init of object with sprite - pygames requirement
class Wall(pygame.sprite.Sprite):

    # procedure of printing object properties when called by matrix
    def __repr__(self):
        return "X"

    # init of object with coordinates in simulation
    def __init__(self, x, y):

        # call init of parent class
        pygame.sprite.Sprite.__init__(self)

        # init graphics with object's sprite - do not touch!
        init_graphics(self, x, y, "wall")

        # real coordinates of object
        self.x = x
        self.y = y

    def next_round(self):
        pass

    def activated(self):
        # serve object:
        print("Wall: Walking on the walls is prohibited, punk.\nGet out of " + str(self.x) + "," + str(self.y))
