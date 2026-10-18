'''
Create a mixed list containing integers, floating-point numbers, and strings (e.g., [10, "Hello", 3.14, "World", 42]). Use a for loop and the type() function inside an if-elif-else block to separate the elements into three distinct lists (one for each data type). Print all three resulting lists.
'''

data = [10, "Hello", 3.14, "World", 42, 2.5]
integer = []
float = []
string = []

for item in data:
   if type(item) == int:
        integer.append(item)
   elif type(item) == float:
        float.append(item)
   elif type(item) == str:
        string.append(item)

print("Integers:", integer)
print("Floats:", float)
print("Strings:", string)
