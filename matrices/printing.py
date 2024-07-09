matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for row in range(len(matrix)):
    # print elements that are inside this column
    for culumn in range(len(matrix[row])):
        print(matrix[row][culumn], end=" ")
    print() # skip a line
    
print() # skip a line

    
# or
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()