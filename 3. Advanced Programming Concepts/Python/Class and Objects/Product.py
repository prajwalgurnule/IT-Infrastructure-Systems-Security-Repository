class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        print(f"Product Name : {self.name}\t Price : {self.price}")
        if self.price > 1500:
            self.price = self.price * 0.90
            print(f"Discount Applied. Your new price is - {self.price}")
        else :
            print("No Discount Applied")

print("Your Cart")
prod1 = Product("Wireless Earphone", 1500)
prod1.apply_discount()
prod2 = Product("Laptop", 45000)
prod2.apply_discount()