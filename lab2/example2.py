x = float(input("write one number. "))
y = float(input("write another number. "))
z = float(input("write third number. "))

if x < y and x < z :
	print(x)

elif y < x and y < z :
	print(y)

else :
	print(z)