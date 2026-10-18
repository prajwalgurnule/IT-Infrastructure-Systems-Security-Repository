'''
Create a list with several duplicate string entries (e.g., ["Delhi", "Mumbai", "Pune",
"Mumbai", "Delhi"]). Create a new empty list. Loop through the original list and use an if
condition with
'''

cities = ["Delhi", "Mumbai", "Pune", "Mumbai", "Delhi"]
unique_cities = []

for city in cities:
  if city not in unique_cities:
    unique_cities.append(city)

print("Unique Cities : ",unique_cities)
