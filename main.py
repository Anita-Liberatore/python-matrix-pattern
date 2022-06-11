import create_matrix
import find

# This main file is point of start to the projet

# Print matrix from file
matrix = []

matrix = create_matrix.create_matrix_from_file()

if matrix.any():
    print(matrix)
else:
    print("Matrix is empty")

result_find = []

find.find_all_single_element(0, matrix)