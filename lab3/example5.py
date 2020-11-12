month = int(input("enter month: "))
day = int(input("enter day: "))

if month == 3:
	if day >= 20:
		print("spring")
	else:
		print("winter")
elif 3 < month < 6:
	print("spring")
elif month == 6:
	if day < 21:
		print("spring")
	else:
		print("summer")
elif 6 < month < 9:
	print("summer")
elif month == 9:
	if day < 22:
		print("summer")
	else:
		print("fall")
elif month == 12:
	if day < 21:
		print("fall")
	else:
		print("winter")
else:
	print("winter")
