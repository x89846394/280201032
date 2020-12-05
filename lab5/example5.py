number = int(input("How many numbers do you want to generate?: "))
f = [0, 1]
for i in range(number-1):
    num = f[-1] + f[-2]
    f.append(num)

f.remove(0)
print(str(f)[1:-1])