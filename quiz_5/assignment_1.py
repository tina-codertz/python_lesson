# creating a class
class Smartphone:
    # class variable
    brand = "Generic"  # class variable

    # method
    def call(self,number):
        self.number = number  # instance variable
        print(f'calling {number} from {self.brand} smartphone')

    # using __init__ method as a constructor
    def __init__(self, brand, model):
        self.brand = brand  # instance variable
        self.model = model  # instance variable

class MySmartphone(Smartphone):
    pass

smart = MySmartphone("Apple", "iPhone 14")
print(smart.model)
smart.call("123-456-7890")  # calling the method with an instance variable