a = int(input("write a number: "))
b = int(input("write another number: "))

power = 1
for i in range(b):
	power *= a

print(power)