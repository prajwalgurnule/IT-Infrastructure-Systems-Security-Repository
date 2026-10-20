class TrainTicket:
    def __init__(self, passanger_name, age):
        self.passanger_name = passanger_name
        self.age = age

passanger_list = []
sample_input = [("Amit", 20), ("Rahul", 30),("Swati",25)]
count = 0
while (count < 3):
    name, age = sample_input[count]
    print(f"Input Recieved - Name : {name}, Age : {age}")
    ticket = TrainTicket(name, age)
    passanger_list.append(ticket)
    count += 1

print("Passanger Travelling in Train")
for pas in passanger_list:
    print(f"Passanger Name : {pas.passanger_name}, Age : {pas.age}")