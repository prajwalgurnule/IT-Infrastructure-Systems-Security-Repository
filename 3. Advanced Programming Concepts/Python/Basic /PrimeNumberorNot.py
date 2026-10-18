
'''
Use for/while loop and If-else condition in program. Write a Python script to read an integer from the user and check whether it is a prime number or not. Ensure the program handles edge cases like numbers less than or equal to 1.
'''

num = int(input("Enter a number : "))
if (num <= 1):
  print(f"{number} is a prime number")

else :
  is_prime = True
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      is_prime = False
      break

  if is_prime:
    print("The number is prime")
  else:
    print("The number is not prime")
