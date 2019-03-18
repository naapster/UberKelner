# kelner object

from scripts.matrix import *
from scripts.dinning_table import *
from scripts.furnace import *
import pygame
from pygame.locals import *

class Waiter(pygame.sprite.Sprite):

    def __init__(self, matrix_fields, num_tables, num_furnaces):

        if num_tables + num_furnaces + 1 > N*N:
            print("Not enough space in restaurant for objects!")

        # init restaurant map - integer matrix with ids of objects
        self.restaurant = Matrix(N, N)

        # data lists containing coordinates of restaurant, for collision purpose only
        self.dining_tables = []
        self.furnaces = []

        # set random coordinates of object
        self.x = matrix_fields[0][0]
        self.y = matrix_fields[0][1]

        # init graphics - do not touch!
        init_graphics(self, self.x, self.y, "waiter")

        # add objects to restaurant - creates waiters, tables and furnaces basing on random positions in the matrix
        # objects have coordinates like in matrix (0..N, 0..N):
        # add ghostwaiter to restaurant
        self.restaurant.insert('Waiter', self.x, self.y)
        counter = 1
        # add tables
        for i in range(num_tables):
            self.dining_tables.append([matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.restaurant.simple_insert(Dinning_table(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))
        counter += num_tables
        # add furnaces
        for i in range(num_furnaces):
            self.furnaces.append([matrix_fields[i + counter][0], matrix_fields[i + counter][1]])
            self.restaurant.simple_insert(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

    # movement procedure - change position on defined difference of coordinates
    def move(self, delta_x, delta_y):
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        # if movement is allowed by matrix, within restaurant borders and the field is empty:
        if self.restaurant.move(self.x, self.y, new_x, new_y):
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
        for table in self.restaurant.objects_to_list(Dinning_table(0, 0)):
            table.next_round()
        for furnace in self.restaurant.objects_to_list(Furnace(0, 0)):
            furnace.next_round()

        # show me status of simulation
        self.restaurant.print_matrix()