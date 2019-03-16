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
        self.restaurant = [[0] * N for _ in range(N)]

        # data lists containing objects of restaurant
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
            self.restaurant[matrix_fields[i + counter][0]][matrix_fields[i + counter][1]] = "dinner_table"
            self.dining_tables.append(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        counter += num_tables

        for i in range(num_furnaces):
            self.restaurant[matrix_fields[i + counter][0]][matrix_fields[i + counter][1]] = "furnace"
            self.dining_tables.append(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

    # movement procedure - change position on defined difference of coordinates
    def move(self, delta_x, delta_y):
        if self.check_field(self.x + delta_x, self.y + delta_y):
            self.x  = self.x + delta_x
            self.y = self.y + delta_y

    # check if restaurant field if not occupied
    def check_field(self, x, y):
        if x in range(0, N) and y in range(0, N):
            return self.restaurant[x][y] == 0
        return False

    def update_position(self):
        # update waiter sprite localization
        self.rect.x = self.x * blocksize
        self.rect.y = self.y * blocksize

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

        self.update_position()

        # change the environment: - REPAIR!
        # update statuses of restaurant objects
        for table in self.dining_tables:
            table.next_round()
        for furnace in self.furnaces:
            furnace.next_round()

        # show me status of simulation
        #self.print_restaurant()

    # print matrix of statuses in restaurant
    def print_restaurant(self):
        for i in self.restaurant:
            print(*i)
        print("---------------------------")

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