def generateBill(item_name, price, tax_rate = 18):
    total_cost = price + (price * tax_rate/100)
    print(f"Item Name : {item_name} |\t Price : {price} |\t Tax Rate : {tax_rate} |\t"
          f"Tax Rate : {tax_rate} |\t Total Cost : {total_cost:.2f}")

items = [
    ("Rice", 1200, 18),
    ("Cooking Oil", 150, 5),
    ("Wheat Flour", 400, 18)
]

for item,price,tax in items:
    if tax == 18:
        generateBill(item, price, tax_rate = tax)
    else :
        generateBill(item, price)