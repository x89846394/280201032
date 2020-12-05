students = 2
average = []
for i in range(students):
    m1 = float(input("Enter midterm 1 grade: "))
    m2 = float(input("Enter midterm 2 grade: "))
    f = float(input("Enter final grade: "))
    ag = (m1 * 30 / 100) + (m2 * 30 / 100) + (f * 40 / 100)
    average.append(ag)
print(average)