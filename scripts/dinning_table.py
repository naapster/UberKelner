# table object class:

from scripts.__init__ import *


# init of object with sprite - pygames requirement
class DinningTable(pygame.sprite.Sprite):

    # procedure of printing object properties when called by matrix
    def __repr__(self):
        return "Dinning Table"

    # init of object with coordinates in simulation
    def __init__(self, x, y):

        # call init of parent class
        pygame.sprite.Sprite.__init__(self)

        # init graphics with object's sprite - do not touch!
        init_graphics(self, x, y, "dinner_table")

        # real coordinates of object
        self.x = x
        self.y = y

        # states of tables:
        # 0 - empty table,
        # 1 - table waiting for waiter
        self.state = 0

        # what has it ordered?
        # integer numbers as dishes id's
        self.order = 0

        # how long does this table wait?
        # for ai learning purpose - waiter has to minimize time in restaurant
        self.time = 0

    def next_round(self):
        # change the environment:
        # need to think about game goal - when does the table start waiting for waiter? REPAIR!
        self.time += 1
