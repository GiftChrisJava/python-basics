class Student:
    def __init__(self, firstName = "John", lastName = "Doe", age = 15):
        self.__first = firstName
        self.__last = lastName
        self.__age = age
        
    def getName(self):
        return self.__first + " " + self.__last
        
        