from sys import flags
import sys
import create_matrix


def find_all_single_element(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                print("Find at position (i, j): ")
                print(i,j)
                print("\n")

def findHash(arr, col, row):
    hashCol = []
    add = 0
    radix = 256
 
    for i in range(0, col):
 
        for j in reversed(range(0, row)):
            add = add + (radix**(row-j-1) *
                         ord(arr[j][i]))% 101
        hashCol.append(add % 101);
        add = 0
    return hashCol
 
def checkEquality(txt, row, col, flag):
    txt = [txt[i][col:patCol + col]
           for i in range(row, patRow + row)]
 
    if txt == pat:
        flag = 1
        print("Pattern found at", \
              "(", row, ", ", col, ")")
    return flag
     
def colRollingHash(txtHash, nxtRow):
 
    radix = 256

    for j in range(len(txtHash)):
        txtHash[j] = (txtHash[j]*radix \
                      + ord(txt[nxtRow][j]))% 101
        txtHash[j] = txtHash[j] - (radix**(patRow) *
                     ord(txt[nxtRow-patRow][j]))% 101
        txtHash[j] = txtHash[j]% 101
    return txtHash
     
 

def search(txt, pat):
     
    patHash = []
    txtHash = []

    patVal = 0
    txtVal = 0
 
    radix = 256

    flag = 0
     
    txtHash = findHash(txt, txtCol, patRow) 
    patHash = findHash(pat, patCol, patRow)
     
    for i in range(len(patHash)):
        patVal = patVal \
                 + (radix**(len(patHash)-i-1) *
                 patHash[i]% 101)
    patVal = patVal % 101
     
     
    for i in range(patRow-1, txtRow):
        col = 0
        txtVal = 0
         
        for j in range(len(patHash)):
            txtVal = txtVal\
                     + (radix**(len(patHash)-j-1) *
                     txtHash[j])% 101
        txtVal = txtVal % 101
         
        if txtVal == patVal:
            flag = checkEquality(\
                     txt, i + 1-patRow, col, flag)
             
        else:
 
            for k in range(len(patHash), len(txtHash)):
 
                txtVal = txtVal \
                         * radix + (txtHash[k])% 101
                txtVal = txtVal \
                         - (radix**(len(patHash)) *
                         (txtHash[k-len(patHash)]))% 101
                txtVal = txtVal % 101
                col = col + 1
 
                if patVal == txtVal:
                    flag = checkEquality(\
                           txt, i + 1-patRow, col, flag)  
                else:
                    continue
                 
        if i + 1<txtRow:
            txtHash = colRollingHash(txtHash, i + 1)
             
    if flag == 0:
        print("Pattern not found")
     
 
print("-----------")
matrix = []
print("MATRIX")
matrix = create_matrix.create_matrix_from_file('input.txt')
print(matrix)

print("PATTERN")

pattern = create_matrix.create_matrix_from_file('pattern.txt')
print(pattern)


input_number_format = create_matrix.create_matrix_from_file('input.txt')
        
res_input = [[str(ele) for ele in sub] for sub in input_number_format]

pattern_number_format = create_matrix.create_matrix_from_file('pattern.txt')
        
res_pattern = [[str(ele) for ele in sub] for sub in pattern_number_format]
        
txt = res_input 
        
pat = res_pattern
        
txtRow = len(input_number_format)
txtCol = len(input_number_format[0])
        
patRow = len(pattern_number_format)
patCol = len(pattern_number_format[0])
        
search(txt, pat)

def query_yes_no(question):

    question = "Do you want to rotate the matrix? [y/n] "
    question_rotate = "How many degres do you want to rotate? "

    active = True
    while active:
        sys.stdout.write(question)
        choice = input().lower()

        if choice in 'y':
            active = True
            sys.stdout.write(question_rotate)
            rotate_choice = input().lower()
            print(rotate_choice)
        elif choice in 'n':
            active = False
            print("Program exit")
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

query_yes_no("Do you want to rotate the matrix")