a = float(input("Enter first parameter: "))
b = float(input("Enter second parameter: "))
c = float(input("Enter last parameter: "))

Discriminant = b ** 2 - 4 * a * c
root_one = (-b + Discriminant ** 0.5) / 2 * a
root_two = (-b - Discriminant ** 0.5) / 2 * a

if Discriminant > 0:
	print("There are two real roots.")
	print("First root is", root_one, ".")
	print("Second root is", root_two, ".")
elif Discriminant == 0:
	print("There is one real root.")
	print("The root is", root_one, ".")
else:
    print("There are two complex roots.")
    print("First root is", root_one, ".")
    print("Second root is", root_two, ".")
