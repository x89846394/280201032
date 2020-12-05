n = int(input("n: "))
l = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input("Enter number: ")))
        if i == j:
            l.append(row[i])

l = sum(l)
print(l)