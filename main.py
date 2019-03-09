
# main game script controller:

# init
from scripts.__init__ import *

# matrix
from scripts.matrix import Matrix

# kelner
from scripts.kelner import Kelner







if __name__ == '__main__':
    mat = Matrix(N, N)
    mat.print_matrix()
    mat.insert_object('asdasd', 2, 4, debug=True)
    mat.insert_object(Matrix(2, 2, fill=5), 1, 1)
    mat.print_matrix()
    print(mat.objects_to_list('asdasd'))
    mat.delete_object(1, 1, debug=True)
    mat.print_matrix()