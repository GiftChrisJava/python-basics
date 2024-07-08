matrix = []

numberOfRows = input("Enter the number of rows : ")
numberOfColumns = input("Enter the number of columns : ")

for row in range(int(numberOfRows)):
    matrix.append([]) # add a new row
    
    for culumn in range(int(numberOfColumns)):
        value =  input("Enter an element and press Enter: ")
        matrix[row].append(value)

print(matrix)