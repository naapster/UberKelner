# furnace object class:

from scripts.__init__ import *


# init of object with sprite - pygames requirement
class Furnace(pygame.sprite.Sprite):

    def __repr__(self):
        return "Furnace"

    def __init__(self, x, y):

        ## init graphics with object's sprite - do not touch!
        init_graphics(self, x, y, "furnace")

        # real coordinates of object
        self.x = x
        self.y = y

        # lists with data
        self.orderedDishes = {}
        self.readyDishes = {}

        self.time = 0

    def next_round(self):
        # change the environment:
        self.time += 1

