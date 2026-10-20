class ShoppingCart:
    def __init__(self):
        self.item = []

    def add_item(self, item_name):
        self.item.append(item_name)
        print(f"Added {item_name} ")

    def display_items(self):
        print("\nItem in shopping cart - ")
        for item in self.item:
            print(f" - {item}")

cart = ShoppingCart()
cart.add_item("Milk")
cart.add_item("Fruits")
cart.add_item("Bread")
cart.display_item()