'''
Use for/while loop and If-else condition in program. Write a program that iterates through a specific range of years. Calculate and print all the leap years from the year 1850 up to 2026.
'''
print("Leap year from 1860 to 2026 : \n")
leap_year = []
for year in range(1850,2026):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0 ):
    leap_year.append(year)

for i in range(0, len(leap_year), 9):
  line = leap_year[i:i + 9]
  print(", ".join(map(str, line)))
print("the leap year are : ",leap_year)
