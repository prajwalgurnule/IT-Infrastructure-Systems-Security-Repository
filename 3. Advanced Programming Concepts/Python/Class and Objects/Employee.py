class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display(self):
        print(f"Employee ID : {self.emp_id} |\t Name : {self.name} |\t Department : {self.department}")

e1 = Employee(1,"Prajwal","Cyber Security")
e1.display()
e2 = Employee(2,"Aditya","Devops Engineer")
e2.display()
e3 = Employee(3,"Piyush","Software Developer")
e3.display()