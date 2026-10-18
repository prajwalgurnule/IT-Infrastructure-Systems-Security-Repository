'''
Create a list containing the names of your 5 favourite Indian cities. Use a for loop to iterate through the list and print each city's name along with its sequence number (e.g., "1. Pune").
'''

city = ["Mumbai","Nagpur","Delhi","Pune","Kolkata"]

for i in range(len(city)):
  print(f"{i+1} - {city[i]}")
