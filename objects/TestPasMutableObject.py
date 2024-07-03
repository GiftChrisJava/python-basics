from circle import Circle

def main():
    # create a circel object of radius 1
    myCircle = Circle()
    
    n = 5
    printAreas(myCircle, n)
    
    print("\nRadius is", myCircle.radius)
    print("n is",n)

#print a table of areas for radius
def printAreas(c, times):
    print("Radius \t\tArea")
    
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius += 1
        times -= 1
        
main()