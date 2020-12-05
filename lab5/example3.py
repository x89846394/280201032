num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
count = 0

while True:
    if num_1 % 10 == num_2 % 10:
        count += 1
    num_1 = num_1 // 10
    num_2 = num_2 // 10
    if num_1 == 0 or num_2 == 0:
        break

print(count)