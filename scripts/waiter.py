# kelner object

from scripts.dinning_table import *
from scripts.matrix import *
from scripts.furnace import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # init graphics - do not touch!
        init_graphics(self, x, y, "waiter")

        # real coordinates of object
        self.x = x
        self.y = y

        # lists with data:
        #dishes lists
        self.orderedDishes = {}
        self.readyDishes = {}

        # objects have coordinates like in matrix (0..N, 0..N)
        # list with furnaces
        self.furnaces = [Furnace(0, 1), Furnace(0,2)]

        # init tables: - need to update this to be more random!
        self.tables = [Dinning_table(2, i) for i in range(N)]

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
        self.x = self.furnaces[0].x
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