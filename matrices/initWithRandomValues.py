import random
matrix = []

numberOfRows = input("Enter the number of rows : ")
numberOfColumns = input("Enter the number of columns : ")

for row in range(int(numberOfRows)):
    matrix.append([])  # Add an empty new row
    
    for column in range(int(numberOfColumns)) :
        matrix[row].append(random.randint(0, 99))

print(matrix)