books = [['Python for beginners',500], ['Blackbook for java',900],[ 'java for dummies', 1000], ['aa',100]]

books.sort()
print(books)
books.sort(key=lambda item: item[1])
print(books)

min_price = min(books, key = lambda item:item[1])
print(min_price)

max_price = max(books, key = lambda item:item[1])
print(max_price)

filtered = list(filter(lambda item:item[1]>500, books))
print(filtered)

mapped = list(map(lambda item:[item[0].title(),item[1]], books))
print(mapped)


colour_Date = [{'name':'red', 'rating':65},
               {'name':'green', 'rating':75},
               {'name':'blue', 'rating':85},
               {'name':'yellow', 'rating':95}]


sort_by_rating = sorted(colour_Date, key = lambda item:item['rating'])
sort_by_rating.reverse()
# print(sort_by_rating)

filtered = list(filter(lambda item:item['rating'] > 80, colour_Date))
# print(filtered)                




# mapped = list(map(lambda index, item:[item[0].title(),item[1]], enumerate(books)))
# print(mapped)


extract = [colour_Date.count([1]) for item in colour_Date]
print(extract)
