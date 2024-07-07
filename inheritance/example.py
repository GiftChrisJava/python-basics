class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        
    def printName(self):
        print(self.firstName, self.lastName)
