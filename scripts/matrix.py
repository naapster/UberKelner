
# matrix object class
import copy

class Matrix:
    #konstruktor, ustawia ilosc szeregow i kolumn, mozna rowniez ustawic co ma byc podstawowym zapelnieniem macierzy, jezeli nie zmienione to zero
    def __init__(self, rows, columns, fill=0):
        self.fill = fill
        self.matrix = [[self.fill for x in range(columns)] for y in range(rows)]

    def __repr__(self):
        #funkcja repr pozwala na ladne drukowanie macierzy, mozna zrobic print(Matrx) i zobaczymy ladna macierz
        s = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        represent = '\n'.join(table)
        return represent

    def print_matrix(self):
        #zbedne gdy mamy repr ale nadal dodalem, mozna wydrukowac macierz metoda, jak kto woli
        s = [[str(e) for e in row] for row in self.matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        print("------------------------------------")

    def insert_object(self, object_to_insert, row, column, debug=False):
        #wklada obiekt na podane miejsce do macierzy
        try:
            self.matrix[column][row] = object_to_insert

            if debug:
                print('Added {0} to matrix[{1}][{2}]'.format(object_to_insert, row, column))
        except IndexError:
            print("ERROR: Index out of bounds. Inserting object is not possible.")

    def delete_object(self, row, column, debug=False):
        #usuwa obiekt i zastepuje go 0, do poprawy
        try:
            deleted_object = self.matrix[row][column]
            self.matrix[row][column] = self.fill

            if debug:
                print('Deleted {0} from matrix[{1}][{2}]'.format(deleted_object, row, column))
        except IndexError:
            print('ERROR: Index out of bounds. Deleting object is not possible.')

    def objects_to_list(self, wanted_object):
        #zwraca liste obiektow i ich miejsc w macierzy, porownywany jest typ obiektu, nie jego wartosc
        list_of_wanted_objects = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if type(self.matrix[i][j]) is type(wanted_object):
                    #list_of_wanted_objects.append((self.matrix[i][j], (i, j)))
                    list_of_wanted_objects.append((self.matrix[i][j]))

        return list_of_wanted_objects

    def get_matrix(self):
        to_return = copy.deepcopy(self.matrix)
        return to_return

    def get_empty_space_type(self):
        return self.fill

if __name__ == '__main__':
    mat = Matrix(30, 30, fill='X')
    print(mat)
    print(mat.get_matrix())