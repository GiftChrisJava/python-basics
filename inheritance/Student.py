from Person import Person # import main parent class

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationYear = 2019
        
    def welcome(self):
        print("welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)