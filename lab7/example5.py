password = input("Enter password: ")
if len(password) >= 8:
    if not any(char.isupper() for char in password):
        print("invalid")
    else:
        if not any(char.islower() for char in password):
            print("invalid")
        else:
            if not any(char.isdigit() for char in password):
                print("invalid")
            else:
                print("valid")
else:
    print("invalid")
