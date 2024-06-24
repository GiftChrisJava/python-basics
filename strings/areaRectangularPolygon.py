import math

#enter the number of sides
numberOfSides = eval(input("Enter the number of sides : "))

#enter side length
sideLength = eval(input("Enter the side : "))

area = (numberOfSides * pow(sideLength, 2)) / (4 * math.tan(math.pi / numberOfSides))

print("The area of the polygon is ", area)