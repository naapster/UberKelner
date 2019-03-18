# kelner object

from scripts.matrix import *
from scripts.dinning_table import *
from scripts.furnace import *
from scripts.__init__ import *
import pygame
from pygame.locals import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, matrix_fields, num_tables, num_furnaces):

        if num_tables + num_furnaces + 1 > N*N:
            print("Not enough space in restaurant for objects!")

        # init restaurant map - integer matrix with ids of objects
        self.restaurant = Matrix(N,N)

        # data lists containing coordinates of restaurant, for collision purpose only
        self.dining_tables = []
        self.furnaces = []

        # set random coordinates of object
        self.x = matrix_fields[0][0]
        self.y = matrix_fields[0][1]

        # init graphics - do not touch!
        init_graphics(self, self.x, self.y, "waiter")

        # add objects to restaurant - creates waiters, tables and furnaces basing on random positions in the matrix
        # objects have coordinates like in matrix (0..N, 0..N)

        counter = 1

        for i in range(num_tables):
            self.dining_tables.append([matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.restaurant.insert_object(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                          matrix_fields[i + counter][0], matrix_fields[i + counter][1], debug=True)

        counter += num_tables

        for i in range(num_furnaces):
            self.furnaces.append([matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.restaurant.insert_object(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]),
                                          matrix_fields[i + counter][0], matrix_fields[i + counter][1], debug=True)

    # movement procedure - change position on defined difference of coordinates
    def move(self, delta_x, delta_y):
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        # if movement is within restaurant borders
        if new_x in range(0, N) and new_y in range(0, N):
            # and the field is empty
            if [new_x, new_y] not in self.dining_tables and [new_x, new_y] not in self.furnaces:
                # set new coordinates
                self.x = new_x
                self.y = new_y
                # update waiter sprite localization after changes
                self.rect.x = self.x * blocksize
                self.rect.y = self.y * blocksize

            # if restaurant field is not empty, analize the environment - take dishes or order - REPAIR
            # else:

    def next_round(self, key):
        # list of events on keys:
        if key == K_RIGHT:
            self.move(1, 0)
        elif key == K_LEFT:
            self.move(-1, 0)
        elif key == K_DOWN:
            self.move(0, 1)
        elif key == K_UP:
            self.move(0, -1)

        # change the environment: - REPAIR!
        # update statuses of restaurant objects
        for table in self.restaurant.objects_to_list(Dinning_table):
            table.next_round()
        for furnace in self.restaurant.objects_to_list(Furnace):
            furnace.next_round()

        # show me status of simulation
        self.restaurant.print_matrix()

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