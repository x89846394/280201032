l = []
n = int(input("How many number?: "))

for i in range(n):
    item = int(input("Enter number: "))
    l.append(item)

unique = []
for element in l:
    if element not in unique:
        unique.append(element)

descending_unique = sorted(unique, reverse=True)
print(descending_unique)