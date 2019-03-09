# kelner object

from scripts.__init__ import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, x, y, window_width, window_height):
        pygame.sprite.Sprite.__init__(self)

        self.window_width = window_width
        self.window_height = window_height

        # lists with data
        self.orderedDishes = {}
        self.readyDishes = {}

        #self.image = pygame.image.load("images/elsa.png")

        self.rect = self.image.get_rect()

        # coordinates x y global
        self.rect.x = x
        self.rect.y = y

    # movement procedures stolen from Elsa
    def move_right(self):
        if self.rect.x + 1 <= N:
            self.rect.x += 1

    def move_left(self):
        if self.rect.x - 1 >= 0:
            self.rect.x -= 1

    def move_down(self):
        '''
        if self.rect.y + self.rect.height + self.step <= self.window_height:
            self.rect.y += self.step
        '''

    def move_up(self):
        '''
        if self.rect.y >= self.step:
            self.rect.y -= self.step
        '''

    def reset(self):
        '''
        self.rect.x = 0
        self.rect.y = 0
        '''