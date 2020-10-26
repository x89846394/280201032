x = float(input("What is your GPA? "))
y = float(input("What is the number of lectures you take? "))

if x < 2.0 and y < 47 :
	print("Not enough number of lectures and GPA!")

elif x < 2.0 and y >= 47 :
	print("Not enough GPA!")

elif x >= 2.0 and y < 47 :
	print("Not enough number of lectures!")

else :
	print("GRADUATED!!!")