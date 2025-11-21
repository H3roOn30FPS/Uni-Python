# Create a class Vehicle with attributes type and fuel. 
# Create a method printInfo that prints all the information.
# Create a class Car (with brand, model, color, year) which inherits from Vehicle.
# Add the methods printInfo and change_color to it.

class Vehicle:
    def __init__(self, v_type, fuel):
        self.v_type = v_type
        self.fuel = fuel

    def printInfo(self):
        print(self.v_type, self.fuel)
###
###
class Car(Vehicle):
    def __init__(self, v_type, fuel, brand, model, color, year):
        super().__init__(v_type, fuel)
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    
    def printInfo(self):
        print(self.brand, self.model, self.color, self.year)
    
    def change_color(self):
        new_color = input("Change color to...:")
        self.color = new_color
###
###
car_1 = Car("Sedan", "Disel", "Mercedes", "S69", "Black", 2019)
car_1.printInfo()
car_1.change_color()
car_1.printInfo()

car_2 = Vehicle("SUV", "Gas")
car_2.printInfo()