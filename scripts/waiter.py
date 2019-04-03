# agent object class:

from scripts.matrix import *
from scripts.dinning_table import *
from scripts.furnace import *
import pygame
import sys
from pygame.locals import *


# init of object with sprite - pygames requirement
class Waiter (pygame.sprite.Sprite):

    # procedure of printing object properties when called by matrix
    def __repr__(self):
        return "Waiter"

    # initialize agent with list of coordinates for tables and furnaces and their number
    def __init__(self, matrix_fields, num_tables, num_furnaces, num_walls):

        # call init of parent class
        pygame.sprite.Sprite.__init__(self)

        # check if there is enough space for everyting in simulation
        if num_tables + num_furnaces + 1 > N*N:
            print("Not enough space in restaurant for objects!")
            sys.exit("N-space overflow")

        # init restaurant - matrix of objects
        self.restaurant = Matrix(N, N)

        # set random coordinates of agent
        self.x = matrix_fields[0][0]
        self.y = matrix_fields[0][1]

        # init graphics with object's sprite - do not touch!
        init_graphics(self, self.x, self.y, "waiter")

        # add objects to restaurant - creates tables and furnaces basing on random positions in the matrix
        # objects have coordinates like in matrix (0..N, 0..N):

        # add ghostwaiter to restaurant to mark waiters position
        self.restaurant.insert('Waiter', self.x, self.y)

        # counter counts number of used coordinates, so no object will occupy the same space in simulation
        counter = 1

        # add tables
        for i in range(num_tables):
            self.restaurant.simple_insert(DinningTable(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        # increase counter with number of used coordinates
        counter += num_tables

        # add furnaces
        for i in range(num_furnaces):
            self.restaurant.simple_insert(Furnace(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        # increase counter with number of used coordinates
        counter += num_furnaces

        # add furnaces
        for i in range(num_walls):
            self.restaurant.simple_insert(DinningTable(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

    # movement procedure - change position of agent on defined difference of coordinates
    def move(self, delta_x, delta_y):
        # temporarily set new coordinates
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
        # add rules here!
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

        # DIAGRAM SEQUENCE HERE! - ADD IN NEXT VERSION!
        # if if if if

        # change the environment: - REPAIR!
        # update statuses of all restaurant objects
        for _ in self.restaurant.all_objects_to_list():
            _.next_round()

        # show me status of simulation - for development purpose only
        print(self.restaurant)
