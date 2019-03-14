from scripts.dinning_table import *
from scripts.matrix import *
from scripts.furnace import *
from scripts.waiter import *
from random import shuffle

class Restaurant(pygame.sprite.Sprite):
    def __init__(self, num_tables, num_furnaces):

        # init restaurant map
        self.space = Matrix(N, N)

        #init waiter
        self.Uber = Waiter(0,0)

        # objects have coordinates like in matrix (0..N, 0..N)
        ##################
        # init tables and furnaces
        # creates tables and furnaces based on random positions in the matrix
        positions = range(N)
        matrix_fields = [[posX, posY] for posX in positions for posY in positions]
        shuffle(matrix_fields)

        #add tables to restaurant - REPAIR!
        for i in range(num_tables):
            self.space.insert_object(Dinning_table(matrix_fields[i][0], matrix_fields[i][1]), matrix_fields[i][0], matrix_fields[i][1])
        for i in range(num_furnaces):
            self.space.insert_object(Furnace(matrix_fields[i + num_tables][0], matrix_fields[i + num_tables][1]), matrix_fields[i + num_tables][0], matrix_fields[i + num_tables][1])
        ##################

    def next_round(self):

        # change the environment:
        # update statuses of restaurant objects
        for object in self.space:
            # update environment
            object.next_round()
            # change environment in space
            #self.space.insert_object(furnace.time, furnace.y, furnace.x)

        # update statuses of tables
        for table in self.tables:
            # update environment
            table.next_round()
            # change environment in space
            self.space.insert_object(table.time, table.y, table.x)

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
