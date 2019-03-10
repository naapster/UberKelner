# kelner object

from scripts.__init__ import *
from scripts.dinning_table import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # init graphics
        pygame.sprite.Sprite.__init__(self)
        # set image
        self.image = pygame.image.load("images/waiter.png")
        #resize image to blocksize
        self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
        # set coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # lists with data
        self.orderedDishes = {}
        self.readyDishes = {}

        # actual coordinates of waiter
        self.x = x
        self.y = y

        # coordinates of kitchen - waiter always starts in kitchen
        self.kitchen_x = self.x
        self.kitchen_y = self.y

        # init tables:
        self.tables = [Dinning_table(300, i * 100) for i in range(3)]

    # movement procedures
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
        self.x = self.kitchen_x
        self.y = self.kitchen_y