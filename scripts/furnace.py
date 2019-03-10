from scripts.__init__ import *

class Furnace(pygame.sprite.Sprite):
    def __init__(self, x, y):

        # init graphics - do not touch!
        init_graphics(self, x, y, "furnace")

        # real coordinates of object
        self.x = x
        self.y = y

        #można dodać jeszcze zmienną trzymającą ilość posiłków ale chyba na razie nie jest to potrzebne
        # lists with data
        self.orderedDishes = {}
        self.readyDishes = {}

        self.time = 0

    def next_round(self):
        # change the environment:
        self.time += 1

