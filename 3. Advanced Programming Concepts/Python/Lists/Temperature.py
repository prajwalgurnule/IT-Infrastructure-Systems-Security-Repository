'''
Initialize a list of daily temperatures in Celsius (e.g., 25, 42, 15, 38, 10). Iterate through the list using a for loop. Use an if-else condition to print "[Temperature]°C is Hot" if it is above 35, and "[Temperature]°C is Normal/Cold" otherwise.
'''
temperature = [25, 42, 15, 38, 10]

for temp in temperature:
  if temp > 35:
    print(f"{temp}°C is Hot")
  else:
    print(f"{temp}°C is Cold/Normal")
