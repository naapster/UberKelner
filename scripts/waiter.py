# kelner object

from scripts.__init__ import *

class Waiter():

    def __init__(self, x, y):

        # lists with data
        self.orderedDishes = {}
        self.readyDishes = {}

        # coordinates of kitchen - waiter always starts in kitchen
        self.kitchen.x = self.x
        self.kitchen.y = self.y

        # actual coordinates of waiter
        self.x = x
        self.y = y

    # movement procedures stolen from Elsa
    def move_right(self):
        if self.x + 1 < N:
            self.x += 1

    def move_left(self):
        if self.x - 1 >= 0:
            self.x -= 1

    def move_down(self):
        if self.y + 1 < N:
            self.y += 1

    def move_up(self):
        if self.y - 1 >= 0:
            self.y -= 1

    def reset(self):
        self.x = self.kitchen.x
        self.y = self.kitchen.y