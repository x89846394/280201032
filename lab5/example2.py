number_count = int(input("How many numbers?: "))
even_numbers = ["0", "2", "4", "6", "8"]
even = 0
for i in range(number_count):
    N = input("Enter an integer: ")
    if N[-1] in even_numbers:
        even += 1

percentage = (even / number_count) * 100
print(percentage, "%")
