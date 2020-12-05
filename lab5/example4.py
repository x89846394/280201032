password = "abc123"

while True:
    guess = input("Enter password: ")
    if guess != password:
        if guess == "help":
            print(password[0])
        else:
            print("Wrong")
    else:
        print("Welcome")
        break
