email = "ceng113@example.com"
your_email = input("Write email: ").lower()
y_email = your_email.split("@")
y_email[0] = y_email[0].replace(".", "")
e = y_email[0] + "@" + y_email[1]

if e == email:
    print(True)
else:
    print(False)