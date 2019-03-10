# kelner object

from scripts.__init__ import *
from scripts.dinning_table import *
from scripts.matrix import *

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

        # init tables: - need to update this to be more random!
        self.tables = [Dinning_table(2 * blocksize, i * blocksize) for i in range(N)]

        # init restaurant map for waiter
        self.space = Matrix(N, N)

    # movement procedures
    def move_right(self):
        if self.x + 1 < N:
            self.x += 1
            self.update_coordinates()

    def move_left(self):
        if self.x - 1 >= 0:
            self.x -= 1
            self.update_coordinates()

    def move_down(self):
        if self.y + 1 < N:
            self.y += 1
            self.update_coordinates()

    def move_up(self):
        if self.y - 1 >= 0:
            self.y -= 1
            self.update_coordinates()

    def reset(self):
        self.x = self.kitchen_x
        self.y = self.kitchen_y
        self.update_coordinates()

    def update_coordinates(self):
        self.rect.x = self.x * blocksize
        self.rect.y = self.y * blocksize

    def restaurant(self):
        # example usage of matrix, for development purpose only
        self.space = Matrix(N, N)
        self.space.print_matrix()
        self.space.insert_object('asdasd', 2, 4, debug=True)
        self.space.insert_object(Matrix(2, 2, fill=5), 1, 1)
        self.space.print_matrix()
        print(self.space.objects_to_list('asdasd'))
        self.space.delete_object(1, 1, debug=True)
        self.space.print_matrix()