class Vehicle:
    def __init__(self,brand,wheels):
        self.brand = brand
        self.wheels = wheels

    def display(self):
        print("Brand: ",self.brand)
        print("Wheels: ",self.wheels)

v1 = Vehicle("Tata",4)
v1.display()