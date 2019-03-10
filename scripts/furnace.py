from scripts.__init__ import *

class Furnace(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        #set image
        self.image = pygame.image.load("images/Furnace.png")

        # resize image to blocksize
        self.image = pygame.transform.scale(self.image, (blocksize, blocksize))
        # set coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x * blocksize
        self.rect.y = y * blocksize

        #można dodać jeszcze zmienną trzymającą ilość posiłków ale chyba na razie nie jest to potrzebne

