'''
Create a list of 5 different vehicle types. Ask the user to input a vehicle name. Use a for loop and an if-else condition to check if the vehicle exists in the list. If it exists, replace that specific element with "Electric Vehicle" and break the loop. If the loop finishes without finding the item, print a "not found" message. Print the final updated list.
'''

vehicles = ["Car","Bikes","truck","Plane","Bicycle"]

search = input("Enter the vehicle to search - ")
found = False
for i in range(len(vehicles)):
    if vehicles[i].lower() == search.lower():
        vehicles[i] = "Electric Vehicle"
        found = True
        break

if found:
    print("Vehicle updated!")
else:
    print("Vehicle not found.")

print("Final list:", vehicles)
