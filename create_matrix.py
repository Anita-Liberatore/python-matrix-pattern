import random
import numpy as np
# This function create a matrix with random value beetwen 0 a 1 
# Function with params: row and column

def create_matrix(my_row, my_column):
    matrix = [[random.randint(0, 1) for _ in range(my_row)] for _ in range(my_column)]

    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()
    print("")

def create_matrix_from_file(file_name):
    f = open (file_name , 'r')
    matrix = []
    matrix = [line.split() for line in f]
    matrix=np.array(matrix)
    matrix=matrix.astype(np.int)
    return matrix