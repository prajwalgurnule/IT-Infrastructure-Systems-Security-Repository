def greet_user():
    while True:
        name = input("Enter your name : ")
        if name == "quit" or name == "q":
            break
        else:
            print("Welcome " + name)

greet_user()