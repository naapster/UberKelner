# matrix object class
import copy

class Matrix:
    # matrix init, set rows and columns, fill is optional - 0 by default
    def __init__(self, rows, columns, fill=0):
        self.fill = fill
        self.matrix = [[self.fill for x in range(columns)] for y in range(rows)]

    # print matrix content
    def print_matrix(self):
        s = [[str(e).split(' ', 1)[0] for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        print("------------------------------------")

    def __repr__(self):
        self.print_matrix()

    # put object on its own coordinates
    def simple_insert(self, object_to_insert):
        if self.is_empty(object_to_insert.x,object_to_insert.y):
            self.matrix[object_to_insert.x][object_to_insert.y] = object_to_insert
            return True
        else:
            return False

    # put object on coordinates
    def insert(self, object_to_insert, x, y):
        if self.is_empty(x, y):
            self.matrix[x][y] = object_to_insert
            return True
        else:
            return False

    # remove object and set 0 instead - REPAIR
    def delete_object(self, x, y):
        if not self.is_empty(x, y):
            self.matrix[x][y] = self.fill
            return True
        else:
            return False

    # move object form coordinates to new one
    def move(self, x, y, new_x, new_y):
        if not self.is_empty(x,y) and self.is_empty(new_x,new_y):
            self.matrix[new_x][new_y] = self.matrix[x][y]
            self.matrix[x][y] = self.fill
            return True
        else:
            return False

    # returns list of objects and coordinates - checking object class type, not content
    def objects_to_list(self, wanted_object):
        list_of_wanted_objects = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if type(self.matrix[i][j]) is type(wanted_object):
                    list_of_wanted_objects.append((self.matrix[i][j]))
        return list_of_wanted_objects

    # check if coordinates are empty
    def is_empty(self, x, y):
        try:
            return self.matrix[x][y] == self.fill
        except IndexError:
            return False

    # ?
    def get_matrix(self):
        to_return = copy.deepcopy(self.matrix)
        return to_return