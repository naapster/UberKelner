# kelner object

from scripts.matrix import *
from scripts.dinning_table import *
from scripts.__init__ import *
from random import shuffle

class Waiter(pygame.sprite.Sprite):

    def __init__(self, num_tables, num_furnaces):

        # init restaurant map
        self.restaurant = []

        # data lists
        self.dining_tables = []
        self.furnaces = []

        # generate random positions list
        positions = range(N)
        matrix_fields = [[posX, posY] for posX in positions for posY in positions]
        shuffle(matrix_fields)

        # real random coordinates of object
        self.x = matrix_fields[0][0]
        self.y = matrix_fields[0][1]

        # init graphics - do not touch!
        init_graphics(self, self.x, self.y, "waiter")

        #add objects to restaurant - creates waiters, tables and furnaces basing on random positions in the matrix

        # objects have coordinates like in matrix (0..N, 0..N)

        counter = 1
        for i in range(num_tables):
            self.restaurant.append(["dinner_table", matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.dining_tables.append(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        counter += num_tables

        for i in range(num_furnaces):
            self.restaurant.append(["furnace", matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.dining_tables.append(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        '''
        for i in range(num_furnaces):
            self.restaurant.insert_object(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                     matrix_fields[i + counter][0], matrix_fields[i + counter][1])
        ##################'''

    # movement procedures
    def move_right(self):
        if self.x + 1 < N:
            self.x += 1
            self.next_round()

    def move_left(self):
        if self.x - 1 >= 0:
            self.x -= 1
            self.next_round()

    def move_down(self):
        if self.y + 1 < N:
            self.y += 1
            self.next_round()

    def move_up(self):
        if self.y - 1 >= 0:
            self.y -= 1
            self.next_round()

    def update_position(self):
        # update waiter sprite localization
        self.rect.x = self.x * blocksize
        self.rect.y = self.y * blocksize

    def next_round(self):

        self.update_position()

        # change the environment: - REPAIR!
        # update statuses of restaurant objects
        # for object in self.space:
        # update environment
        # object.next_round()

        # show me status of simulation
        #self.space.print_matrix()

    def example(self):
        # example usage of matrix, for development purpose only
        self.space = Matrix(N, N)
        self.space.print_matrix()
        self.space.insert_object('asdasd', 2, 4, debug=True)
        self.space.insert_object(Matrix(2, 2, fill=5), 1, 1)
        self.space.print_matrix()
        print(self.space.objects_to_list('asdasd'))
        self.space.delete_object(1, 1, debug=True)
        self.space.print_matrix()