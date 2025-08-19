# creating a program
class Vehicle:
    def move(self):
        pass

# creating a class
class Car(Vehicle):
    def move(self):
        print("The car is moving")

class plane():
    def move(self):
        print("The plane is flying")

vehicles = [Car(), plane()] 

for v in vehicles:
    v.move()
