# agent object class:

from scripts.matrix import *
from scripts.dinning_table import *
from scripts.furnace import *
from scripts.wall import *
import pygame
import sys
from pygame.locals import *
from main import init_graphics, blocksize
import time


# init of object with sprite - pygames requirement
class Waiter (pygame.sprite.Sprite):

    # procedure of printing object properties when called by matrix
    def __repr__(self):
        return "Waiter"

    # initialize agent with list of coordinates for tables and furnaces and their number
    def __init__(self, n, matrix_fields, num_tables, num_furnaces, num_walls):

        # call init of parent class
        pygame.sprite.Sprite.__init__(self)

        # check if there is enough space for everyting in simulation
        if num_tables + num_furnaces + num_walls + 1 > n*n:
            print("Not enough space in restaurant for objects!")
            sys.exit("N-space overflow")

        # init restaurant - matrix of objects
        self.restaurant = Matrix(n, n)

        # set random coordinates of agent
        self.x = matrix_fields[0][0]
        self.y = matrix_fields[0][1]

        # init graphics with object's sprite - do not touch!
        init_graphics(self, self.x, self.y, "waiter")

        # add objects to restaurant - creates tables and furnaces basing on random positions in the matrix
        # objects have coordinates like in matrix (0..n, 0..n):

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
            self.restaurant.simple_insert(Wall(matrix_fields[i + counter][0], matrix_fields[i + counter][1]))

        # get dfs path and parse it for movement control purpose
        self.dfs_path = []
        self.goals = matrix_fields[1:counter]
        # set AI control variable - change to false when user changes path and the need of recalculation appears
        self.path_control = False

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

        else:
            self.restaurant[new_x][new_y].activated

        # if restaurant field is not empty, analize the environment - take dishes or order - REPAIR
        # add rules here!
        # else:

    def next_round(self, key):

        # check if agent was moved:
        if key in [K_RIGHT, K_LEFT, K_DOWN, K_UP]:
            self.path_control = False

        # list of events on keys:
        if key == K_RIGHT:
            self.move(1, 0)
        elif key == K_LEFT:
            self.move(-1, 0)
        elif key == K_DOWN:
            self.move(0, 1)
        elif key == K_UP:
            self.move(0, -1)

        elif key == K_SPACE:
            # on space pressed, move waiter with dfs method sequence
            # check if waiter was moved out of path:
            if not self.path_control:
                # get dfs path and parse it for movement control purpose
                self.dfs_path = self.get_dfs_path([self.x, self.y], self.goals[0])
                # set AI control variable - change to false when user changes path and the need of recalculation appears
                self.path_control = True

            # move agent on dfs path
            try:
                if self.dfs_path:
                    self.move(self.dfs_path[0][0], self.dfs_path[0][1])
                    self.dfs_path.pop(0)
                else:
                    if self.goals:
                        self.goals.pop(0)
                        self.dfs_path = self.get_dfs_path([self.x, self.y], self.goals[0])
                    else:
                        print("No goals left!")
            except IndexError:
                print("No moves left!")

        # DIAGRAM SEQUENCE HERE! - ADD IN NEXT VERSION!
        # if if if if

        # change the environment: - REPAIR!
        # update statuses of all restaurant objects
        # for _ in self.restaurant.all_objects_to_list():
            # _.next_round()
        # simulation probably won't require changes of environment

        # show me status of simulation - for development purpose only
        # print(self.restaurant)

    # //////////////////////////////////////////////////
    # DFS section
    @staticmethod
    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))

    def get_dfs_path(self, start, goal):
        # measure time
        starttime = time.time()
        print("Agent: DFS path calculation executed...")
        # calculate dfs
        start = ",".join(map(str, start))
        goal = ",".join(map(str, goal))
        # get dfs path and parse it for movement control purpose
        dfs_path = list(self.dfs_paths(self.restaurant.to_graph(), start, goal))
        if len(dfs_path) > 0:
            dfs_path = list(min(dfs_path, key=len))
            # parse list to get coordinates of next moves
            for i in range(len(dfs_path)):
                dfs_path[i] = list(map(int, dfs_path[i].split(',')))
            # calculate movement vectors basing on coordinates
            for i in range(len(dfs_path)-1):
                dfs_path[i][0] = dfs_path[i+1][0] - dfs_path[i][0]
                dfs_path[i][1] = dfs_path[i+1][1] - dfs_path[i][1]
            # remove last move (it can't be executed)
            dfs_path.pop(-1)
        else:
            print("Agent: no dfs path found!")
            dfs_path = [[0, 0]]
        print("Agent: DFS path calculation execution complete after {0:.2f} seconds.".format(time.time() - starttime))
        # return path for agent
        return dfs_path
    # //////////////////////////////////////////////////
