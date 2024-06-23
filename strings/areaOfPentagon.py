#import math module
import math
#enter radius
radius = eval(input("Enter radius of a pentagon : "))

s = 2 * radius * math.sin(math.pi / 5)

areaOfPentagon = ((3 * math.sqrt(3)) / 2) * pow(s,2)

print(f"The area of the pentagon of radius {radius} is {round(areaOfPentagon, 2)}")