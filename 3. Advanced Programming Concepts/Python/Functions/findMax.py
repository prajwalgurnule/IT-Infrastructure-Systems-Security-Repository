def findMax(number_list):
    max = number_list[0]
    for num in number_list:
        if num > max:
            max = num
    return max

print("Find Maximum")
user_list = []
for i in range(5):
    num = int(input(f"Enter the numbers {i+1} - "))
    user_list.append(num)

print("Your List : ",user_list)
max_value = findMax(user_list)
print(f"Maximum Value in the list : {max_value}")