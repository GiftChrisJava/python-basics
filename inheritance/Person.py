class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        
    def printName(self):
        print(self.firstName, self.lastName)

# class Students(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)


# using super
class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2019
    
    def welcome(self):
        print("welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)
        
x = Students("Mike", "Olsen")
x.printName()
print(x.graduationYear)
x.welcome()