employees = {}

for i in range(5):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    employees.update({name:salary})
s = list(employees.values())
a = sorted(s)

for key, value in employees.items():
    if value == a[-1]:
        print(key)
    if value == a[-2]:
        print(key)
    if value == a[-3]:
        print(key)
