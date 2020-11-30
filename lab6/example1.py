l = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]
for elements in l:
    name, age = elements
    if age > 18:
        print(name)