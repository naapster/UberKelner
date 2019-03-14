from scripts.dinning_table import *
from scripts.matrix import *
from scripts.furnace import *
from scripts.waiter import *
from random import shuffle

class Restaurant(pygame.sprite.Sprite):
    def __init__(self, num_waiters, num_tables, num_furnaces):

        # init restaurant map
        self.space = Matrix(N, N)

        ##################
        # generate random positions list
        positions = range(N)
        matrix_fields = [[posX, posY] for posX in positions for posY in positions]
        shuffle(matrix_fields)

        #add objects to restaurant - creates waiters, tables and furnaces basing on random positions in the matrix

        # one special playable waiter
        self.Uber = Waiter(matrix_fields[1][0], matrix_fields[1][1])

        counter = 1
        # objects have coordinates like in matrix (0..N, 0..N)
        for i in range(num_waiters):
            self.space.insert_object(Waiter(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                     matrix_fields[i + counter][0], matrix_fields[i + counter][1])
        counter += num_waiters
        for i in range(num_tables):
            self.space.insert_object(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                     matrix_fields[i + counter][0], matrix_fields[i + counter][1])
        counter += num_tables
        for i in range(num_furnaces):
            self.space.insert_object(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                     matrix_fields[i + counter][0], matrix_fields[i + counter][1])
        ##################

    def next_round(self):
        # change the environment: - REPAIR!
        # update statuses of restaurant objects
        #for object in self.space:
            # update environment
            #object.next_round()

        # show me status of simulation
        self.space.print_matrix()

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
