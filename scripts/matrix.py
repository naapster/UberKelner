# matrix object class
import copy


class Matrix:
    # matrix init, set rows and columns, fill is optional - 0 by default
    def __init__(self, rows, columns, fill="0"):
        self.fill = fill
        self.matrix = [[self.fill for _ in range(columns)] for _ in range(rows)]

    # print matrix content
    def print_matrix(self):
        s = [[str(e) for e in row] for row in self.matrix]
        s = list(map(list, zip(*s)))
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        print("------------------------------------")

    def __repr__(self):
        # funkcja repr pozwala na ladne drukowanie macierzy, mozna zrobic print(Matrx) i zobaczymy ladna macierz
        s = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        represent = '\n'.join(table)
        return represent

    def simple_insert(self, object_to_insert):
        # if space in matrix is empty and new coordinates are empty
        if self.is_empty(object_to_insert.x, object_to_insert.y):
            # insert object to matrix
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
        if not self.is_empty(x, y) and self.is_empty(new_x, new_y):
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
        to_return = copy.deepcopy(self.matrix)
        return to_return