matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

maxRow = matrix[0]
indexOfMaxRow = 0

for row in range(1, len(matrix)):
    if sum(matrix[row]) > sum(maxRow):
        maxRow = matrix[row]
        indexOfMaxRow = row

print("Row", indexOfMaxRow, "has the maximum sum of", maxRow)