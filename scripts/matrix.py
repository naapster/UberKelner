# matrix object class:

import copy

from scripts.dinning_table import *
from scripts.furnace import *


class Matrix:
    # matrix init, set rows and columns, fill is optional - 0 by default
    def __init__(self, rows, columns, fill="_"):
        self.fill = fill
        self.matrix = [[self.fill for _ in range(columns)] for _ in range(rows)]

    # print matrix content beautified when calling print(matrix)
    def __repr__(self):
        s = [[str(e) for e in row] for row in self.matrix]
        # transpose rows
        s = list(map(list, zip(*s)))
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        # return content
        return '\n'.join(table) + '\n' + "------------------------------------"

    # insert object on its own coordinates
    def simple_insert(self, object_to_insert):
        # if space in matrix is empty and new coordinates are empty
        if self.is_empty(object_to_insert.x, object_to_insert.y):
            # insert object to matrix
            self.matrix[object_to_insert.x][object_to_insert.y] = object_to_insert
            return True
        else:
            return False

    # insert object on other coordinates than its own
    def insert(self, object_to_insert, x, y):
        if self.is_empty(x, y):
            self.matrix[x][y] = object_to_insert
            return True
        else:
            return False

    # remove object and set fill instead
    def delete_object(self, x, y):
        if not self.is_empty(x, y):
            self.matrix[x][y] = self.fill
            return True
        else:
            return False

    # move object form coordinates to new one
    def move(self, x, y, new_x, new_y):
        # if there is object to move and new space is not occupied
        if not self.is_empty(x, y) and self.is_empty(new_x, new_y):
            # move object and fill its previous place
            self.matrix[new_x][new_y] = self.matrix[x][y]
            self.matrix[x][y] = self.fill
            return True
        else:
            return False

    # activate object
    # noinspection PyUnresolvedReferences
    def activate(self, x, y):
        try:
            self.matrix[x][y].activated()
        except AttributeError:
            print("Matrix: Trying to activate non-operateable object at: " + str(x) + ", " + str(y))

    # returns list of objects by checking object class type, not content
    def objects_to_list(self, wanted_object):
        list_of_wanted_objects = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if isinstance(self.matrix[i][j], type(wanted_object)):
                    list_of_wanted_objects.append((self.matrix[i][j]))
        return list_of_wanted_objects

    # returns list of all objects - better performance of matrix, no double-checking
    def all_objects_to_list(self):
        list_of_wanted_objects = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if not isinstance(self.matrix[i][j], type(self.fill)) \
                        and not isinstance(self.matrix[i][j], str):
                    list_of_wanted_objects.append((self.matrix[i][j]))
        return list_of_wanted_objects

    # check if coordinates are empty
    def is_empty(self, x, y):
        try:
            return self.matrix[x][y] == self.fill \
                   and x >= 0 and y >= 0
        except IndexError:
            return False

    # return copy of matrix - regular '=' would just set reference to source, not copy the content
    def get_matrix(self):
        return copy.deepcopy(self.matrix)

    # parse matrix to graph understandable for DFS algorithm
    def to_graph(self):
        print("Matrix: converting matrix to graph...")
        graph = dict()
        # list of available connections
        connections = [[type(self.fill), type(self.fill)],
                       [type(self.fill), type(Furnace(0, 0))], [type(self.fill), type(DinningTable(0, 0))]]
        # parse matrix:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                key = "{0},{1}".format(i, j)
                value_list = list()
                for vec in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    try:
                        # add connection between blanks, blank and table, blank and kitchen
                        if (([type(self.matrix[i][j]), type(self.matrix[i + vec[0]][j + vec[1]])] in connections
                                or [type(self.matrix[i + vec[0]][j + vec[1]]), type(self.matrix[i][j])] in connections)
                                and i + vec[0] >= 0 and j + vec[1] >= 0):
                            value_list.append("{0},{1}".format(i + vec[0], j + vec[1]))
                    except IndexError:
                        pass
                graph[key] = set(value_list)
        print("Matrix: converted matrix to graph.")
        return graph

    def to_graph_visited_or_not(self):
        print("Matrix: converting matrix to graph...")
        graph = dict()
        # list of available connections
        connections = [[type(self.fill), type(self.fill)],
                       [type(self.fill), type(Furnace(0, 0))], [type(self.fill), type(DinningTable(0, 0))]]
        # parse matrix:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                key = "{0},{1}".format(i, j)
                value_list = list()
                for vec in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    try:
                        # add connection between blanks, blank and table, blank and kitchen
                        if (([type(self.matrix[i][j]), type(self.matrix[i + vec[0]][j + vec[1]])] in connections
                             or [type(self.matrix[i + vec[0]][j + vec[1]]), type(self.matrix[i][j])] in connections)
                                and i + vec[0] >= 0 and j + vec[1] >= 0):
                            value_list.append("unvisited")
                    except IndexError:
                        pass
                graph[key] = set(value_list)
        print("Matrix: converted matrix to graph.")
        return graph

    def size(self):
        return len(self.matrix)
