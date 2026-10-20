class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

student1 = Student("Prajwal",300)
student2 = Student("Rohan",200)

print("Student Data -")
print(f"Student Name : {student1.name} \t Total Marks : {student1.total_marks}")
print(f"Student Name : {student2.name} \t Total Marks : {student2.total_marks}\n")

if student1.total_marks > student2.total_marks:
    print("Higher Scorer : ",student1.name)
elif student2.total_marks > student1.total_marks:
    print("Higher Scorer : ",student2.name)
else :
    print("Bothe have scored the equal marks")