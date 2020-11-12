edge_1 = float(input("What is the length of the first perpendicular edge?: "))
edge_2 = float(input("What is the length of the second perpendicular edge?: "))

a = (edge_1 ** 2) + (edge_2 ** 2)
b = a ** 0.5

print(f"The hypotenuse is {float(b)}.")