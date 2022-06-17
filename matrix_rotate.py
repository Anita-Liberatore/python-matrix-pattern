def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def rotate180Matrix(mat):     
    N = len(mat[0])
    # rotate the matrix by 180 degrees
    for i in range(N // 2):
        for j in range(N):
            temp = mat[i][j]
            mat[i][j] = mat[N - i - 1][N - j - 1]
            mat[N - i - 1][N - j - 1] = temp

    return mat

def rotare270Matrix(mat):
    new_matrix = []
    for i in range(len(mat[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], mat)))

    return new_matrix

 
def operation(pattern,degree):
    if degree == '90':
        pattern_90 = rotate90Clockwise(pattern)
        return pattern_90
    elif degree == '180':
        pattern_180 = rotate180Matrix(pattern)
        return pattern_180
    elif degree == '270':
        pattern_270 = rotare270Matrix(pattern)
        return pattern_270
    else:
        return "No case"
