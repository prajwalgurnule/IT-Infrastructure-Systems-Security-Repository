'''
Write a script that asks the user to input 5 integer scores, appending each to a list. Use a for loop and if conditions to compare the values, 
find the highest and lowest scores in the list, and print them.
'''
scores = []
for i in range(5):
  num = int(input("Enter the Score - "))
  scores.append(num)

highest = scores[0]
lowest = scores[0]

for score in scores:
  if score > highest:
    highest = score
  elif score < lowest:
    lowest = score

print("Highest Score - ",highest)
print("Lowest Score - ",lowest)
