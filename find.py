def find_all_single_element(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                print("Find at position (i, j): ")
                print(i,j)
                print("\n")