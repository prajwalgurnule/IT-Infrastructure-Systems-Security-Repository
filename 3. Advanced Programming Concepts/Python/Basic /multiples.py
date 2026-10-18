
'''
Use for/while loop in program. Write a script that prompts the user for a number, then uses a for loop to print the first 10 multiples of that number. Rewrite the exact same logic using a while loop instead.
'''

num = int(input("Enter a number : "))
print(f"First 10 multiples of {num} are below :")

# using for loop
print("\nUsing For Loop")
for i in range(1,11):
  multiple = num * i
  print(f"{num} x {i} = {multiple}")


# using while loop
print("\nUsing While Loop")
i = 1
while(i<=10):
  multiple = num * i
  print(f"{num} x {i} = {multiple}")
  i += 1
