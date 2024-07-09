matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for column in range(len(matrix[0])):
    total = 0
    
    for row in range(len(matrix)):
        total += matrix[row][column]
    
    print("Sum for column", column, "is", total)