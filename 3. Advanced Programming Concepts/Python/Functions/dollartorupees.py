def dollartorupees(amount):
    return amount * 83

dollars = [100, 200, 300, 400, 500]
inr_object = map(dollartorupees, dollars)
inr_amount = list(inr_object)

print("USD amounts : ",dollars)
print("INR amounts : ",inr_amount)