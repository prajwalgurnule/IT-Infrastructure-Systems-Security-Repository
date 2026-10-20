def calculate_total_expense(*expenses):
    total = 0
    for exp in expenses:
        total += exp
    if total > 10000:
        print("Warning you have excluded the budget")
    else :
        print("You are in the budget")

print("Call with 3 arguments")
calculate_total_expense(1000,300,4000)
print("Call with 6 arguments")
calculate_total_expense(1000,300,4000, 5000, 100)