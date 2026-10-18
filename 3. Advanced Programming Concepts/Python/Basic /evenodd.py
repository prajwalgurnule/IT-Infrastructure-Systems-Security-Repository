
'''
Use an If-else condition in program. Write a script that asks the user to input an integer.
Use the modulo operator (%) and an if-else block to determine whether the entered number is even or odd, and print the result.
'''

num = int(input("Enter a number : "))
if num % 2 == 0:
  print(f"The {num} is Even number")
else:
  print(f"The {num} is Odd number")
