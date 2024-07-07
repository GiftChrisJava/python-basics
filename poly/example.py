class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("move")

class Car(Vehicle):
    pass

class Boat(Vehicle):    
    def move(self):
        print("Sail")
        
class Plane(Vehicle):    
    def move(self):
        print("Fly")
        
car1 = Car("Ford", "Mustang")
boat = Boat("Ibia", "Touring")
plane = Plane("Boeing", "747")


for x in (car1, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()
