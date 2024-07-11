from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__("yellow", True)
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
        
    def getAreaOfCircle(self):
        return math.pi * math.pow(self.__radius, 2)
    
    def getDiameter(self):
        return 2 * self.__radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.__radius
    
    def printCircle(self):
        print(self.__str__() + " radius " + str(self.__radius))