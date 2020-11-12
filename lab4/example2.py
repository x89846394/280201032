year = int(input("write a year:"))

if year % 100 == 0 and year % 400 != 0:
	print("not leap year")
elif year % 4 == 0:
	print("leap year")
else:
	print("not leap year")
