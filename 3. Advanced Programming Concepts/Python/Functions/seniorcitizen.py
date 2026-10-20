def is_senior_citizen(age):
    if age >= 60:
        return True
    else:
        return False

ages = [10, 60, 70, 50, 45, 45]
senior_citizen_object =  filter(is_senior_citizen, ages)
senior_citizen = list(senior_citizen_object)

print("Ages : ", ages)
print("Senior Citizens : ", senior_citizen)