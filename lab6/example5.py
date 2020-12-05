n = int(input("n: "))
matrix = []
for i in range(n):
    row = []
    matrix.append(row)
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)

for row in matrix:
    print(row)