# defining a class
class Car:
    color = "red"  # class variable

    # method
    def drive(self):
        print('the car is driving')

# creating an object
my_car = Car()
print(my_car.color)  # accessing class variable
my_car.drive()

# constructors
#  __init__ method is a constructor in Python it allows each objrct to start with specififc values

# instance variables are specific to each object and can vary across objects

# setting up constructor
class Car:
    def __init__(self,color,model):
        self.color = color # instance variable
        self.model = model # instance variable

# creating objects with unique attributes
car1 = Car('blue','sedan')
car2 = Car('black','SUV')

print(car1.color)
print(car1.model)
print(car2.color)
print(car2.model)


# OOP pinciples
# encapsulation, inheritance, polymorphism
# inheritance allows classes to inherit attributes and 
# methods from other classes this help reduce code repitionand create a natural hierarchy

class Vehicle:
    def __init__(self, wheels,mirrors):
        self.wheels = wheels
        self.mirrors = mirrors

class Car(Vehicle):  # Car inherits from Vehicle
    pass

car = Car(4,3)
print(car.mirrors)

# polymorphism allows methods to do different things based on the object it is acting upon, classes can  behave 
# differently for the same method inherited from base class
class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
# polymorphism in action
for animal in [Dog(),Cat()]:
    print(animal.speak())  # each animal speaks in its own way


# encapsulation is the bundling of data and methods that operate on that data within a single unit,
#  it restricts direct access to some of an object's components

class SecretStash:
    def __init__(self):
        self.__chocolates = 10 # private variable

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("one Chocolate taken")
        else:
            print("No chocolates left!")

stash = SecretStash()
stash.take_chocolate()  # accessing method to interact with private variable
