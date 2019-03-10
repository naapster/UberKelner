from scripts.__init__ import *

class Dinning_table(pygame.sprite.Sprite):
    def __init__(self, x, y):

        #init graphics
        pygame.sprite.Sprite.__init__(self)
        #set image
        self.image = pygame.image.load("images/dinner_table.png")
        # resize image to blocksize
        self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
        # set coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # states of tables:
        # 0 - empty table,
        # 1 - table waiting for waiter
        self.state = 0

        # what has it ordered?
        # integer numbers as dishes id's
        self.order = 0

        # how long does this table wait?
        # for ai learning purpose - waiter has to minimize time in restaurant
        self.time_waiting = 0




