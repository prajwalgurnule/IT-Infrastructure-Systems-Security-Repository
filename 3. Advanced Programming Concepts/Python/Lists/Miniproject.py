'''
Create a simple daily expense tracker. Use a while loop to continuously prompt the user to input an expense amount in . If the user inputs 0, break the loop. Store all valid expenses in ₹ a list. Once the loop terminates, use a for loop to calculate the total sum of the list. Use an if- else block to print a warning if the total exceeds a predefined budget of ₹5,000, or a success ₹ message if they stayed within budget.
'''

expense = []
budget = 5000
while True:
  amount = float(input("Enter the amount (₹0 to stop) -  "))
  if amount == 0:
    break
  elif amount > 0:
    expense.append(amount)
  else:
    print("Invalid Amount. Try Again")

total = 0
for exp in expense:
  total += exp
print("\nExpenses = ",expense)
print(f"Total = ₹{total:.2f}")
if total > budget:
  print("Warning! You have excluded the budget")
else:
  print("Success. You stayed within budget")
