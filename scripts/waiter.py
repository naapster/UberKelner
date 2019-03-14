# kelner object

from scripts.__init__ import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # init graphics - do not touch!
        init_graphics(self, x, y, "waiter")

        # real coordinates of object
        self.x = x
        self.y = y

        # lists with data:
        self.orderedDishes = {}
        self.readyDishes = {}

    # movement procedures
    def move_right(self):
        if self.x + 1 < N:
            self.x += 1
            self.update_position()

    def move_left(self):
        if self.x - 1 >= 0:
            self.x -= 1
            self.update_position()

    def move_down(self):
        if self.y + 1 < N:
            self.y += 1
            self.update_position()

    def move_up(self):
        if self.y - 1 >= 0:
            self.y -= 1
            self.update_position()

    def update_position(self):
        # update waiter sprite localization
        self.rect.x = self.x * blocksize
        self.rect.y = self.y * blocksize

    def next_round(self):
        self.update_position()