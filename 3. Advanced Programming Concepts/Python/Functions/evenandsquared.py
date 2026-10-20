def even(num):
    return num % 2 == 0

def squared(num):
    return num ** 2

n = list(range(1,21))
evens_filter = filter(even, n)
squared_map = map(squared, evens_filter)
squared = list(squared_map)

print("Original Numbers : ",n)
print("Squared Even Numbers : ",squared)
