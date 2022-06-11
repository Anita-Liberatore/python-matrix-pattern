import create_matrix
import find

# This main file is point of start to the projet

# Print matrix from file
matrix = []

matrix = create_matrix.create_matrix_from_file()
print(matrix)

result_find = []

find.findall(0, matrix)