num = input("write a number: ")

if len(str(num)) >= 2:
	print(int(num[-1]) + int(num[-2]))
else:
    print("0" + str(num))