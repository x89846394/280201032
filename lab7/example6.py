numbers1 = [2, 3, 4, 20, 5, 5, 15]
numbers2 = [10, 20, 20, 15, 30, 40]
set_1 = set(numbers1)
set_2 = set(numbers2)
intersection = []

for element in set_1:
    if element in set_2:
        intersection.append(element)
union = []

for element in set_1:
    union.append(element)
for element in set_2:
    if element not in union:
        union.append(element)
print(set(intersection))
print(set(union))
