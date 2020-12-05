books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
c = []

for el in books:
    d = []
    c.append(d)
    for char in el:
        if char not in d:
            d.append(char)
for i in range(len(books)):
    key = books[i]
    value = (len(books[i]), len(c[i]))
    book_dict.update({key:value})

for j in range(len(books)):
    key = books[j]
    average = float((len(books[j]) + len(c[j])) / 2)
    value = (len(books[j]), len(c[j]), average)
    book_dict.update({key:value})

print(book_dict)