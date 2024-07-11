from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    circle = Circle(1.5)
    
    print("A circle", circle)
    print("The radius is", circle.getRadius())
    print("The area is", circle.getAreaOfCircle())
    print("The diameter is", circle.getDiameter())
    
    
    rectangle = Rectangle(2, 4)
    print(f"\nA rectangle {rectangle}")
    print(f"The area is {rectangle.getAreaRectangle()}")
    print(f"The perimeter is {rectangle.getPerimeter()}")
    
    
    
main()