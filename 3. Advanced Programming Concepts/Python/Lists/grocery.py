'''
Write a script that prompts the user to enter how many items they want to add to a grocery list. Use a for loop to take string inputs from the user exactly that many times, append each item to an empty list, and print the complete list at the end.
'''

basket = []
num = int(input("How many items you want to add in list? - "))
for i in range(num):
  grocery = input("Enter item to add in list - ")
  basket.append(grocery)

print(f"Grocery Items - {basket}")
