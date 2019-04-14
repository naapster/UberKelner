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
import itertools

# set recursion limit:
sys.setrecursionlimit(1500)


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
        self.x, self.y = matrix_fields[0][0], matrix_fields[0][1]

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

        # calculate graph
        self.graph = self.restaurant.to_graph()

        # set list of goals
        self.goals = matrix_fields[1:counter]

        # set permutations of goals
        self.goalsPer = list(map(list, list(itertools.permutations(self.goals))))

        # set list of solutions
        self.solutions = []

        # set dfs solution
        self.dfs_path = []

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
            # activate object you tried to move on
            self.restaurant.activate(new_x, new_y)

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
                # get dfs path
                self.get_dfs_path()
                print("Solution results")
                print(self.solutions)

                # choose the shortest solution of restaurant and parse it to movement vector
                self.dfs_path = list(min(self.solutions, key=len))
                if len(self.dfs_path) > 0:
                    # parse list to get coordinates of next moves
                    print(self.dfs_path)
                    self.dfs_path = self.calculate_vector_movement(self.dfs_path)
                else:
                    print("Agent: no dfs path found!")

                # set AI control variable - change to false when user changes path and the need of recalculation appears
                self.path_control = True

            # move agent on dfs path
            if self.dfs_path:
                self.move(self.dfs_path[0][0], self.dfs_path[0][1])
                self.dfs_path.pop(0)
            else:
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

    # parser of list of lists of coordinates to list of lists of moves
    @staticmethod
    def calculate_vector_movement(list_):
        # calculate movement vectors basing on coordinates
        for i in range(len(list_) - 1):
            list_[i][0] = list_[i + 1][0] - list_[i][0]
            list_[i][1] = list_[i + 1][1] - list_[i][1]
        # remove last move (it can't be executed)
        list_.pop(-1)
        return list_

    # //////////////////////////////////////////////////
    #           S O L U T I O N S
    # //////////////////////////////////////////////////

    # DFS
    @staticmethod
    def parse_dfs_list(list_):
        # parse list to get coordinates of next moves
        for e in list_:
            for i in range(len(e)):
                e[i] = list(map(int, e[i].split(',')))
        # make list from list of lists
        list_ = [item for sublist in list_ for item in sublist]
        return list_

    def caluclate_dfs_path(self, graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    # add path - REPAIR
                    self.dfs_path.append(path)
                    # remove goal and calculate next path
                    self.goals.pop(0)
                    if self.goals:
                        # call next goal
                        self.caluclate_dfs_path(self.graph, next_, str(self.goals[0][0]) + "," + str(self.goals[0][1]))
                else:
                    stack.append((next_, path + [next_]))

    def get_dfs_path(self):
        # measure time
        starttime = time.time()
        print("Agent: DFS path calculation executed...")
        # for all permutations of goals list: (loosing info about primary goals)
        for self.goals in self.goalsPer:
            # calculate dfs
            start = str(self.x) + "," + str(self.y)
            goal = str(self.goals[0][0]) + "," + str(self.goals[0][1])
            self.caluclate_dfs_path(self.graph, start, goal)
            # add parsed dfs_path to solutions
            self.solutions.append(self.parse_dfs_list(self.dfs_path))
            # clear dfs_path and run next permutation
            self.dfs_path = []
        # now self.solutions contains all solutions of dfs
        print("Agent: DFS path calculation execution complete "
                "after {0:.2f} seconds.".format(time.time() - starttime))
    # //////////////////////////////////////////////////
