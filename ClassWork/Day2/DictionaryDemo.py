weather_date = {
    'Pune':[23,28],
    'Bombay':[34,38],
'Delih':[36,40]
}

emp = {'name':'nikhil',
       'age':30,'salary':10000000000,
                'skills' : ['Python','C++','Java'],}

print('Pune' in weather_date)
print('Pune' not in emp)

for key,val in weather_date.items() :
    print(key, val)


books = {'Python for beginners':500, 'Blackbook for java':900, 'java for dummies': 1000}
#books.sort()
print(books)
item_dict = {item[0]: len(item[0]) for item in books}
print(item_dict.items())
# lst = sorted(item_dict)
# print(lst)


#to print a dictionary with book name andprice
# def nikhil(lst, disc):
#     lst = {item[0] : item[1]*disc for item in books}
#     return lst
# print(nikhil(books,0.7))

#item_dict = {item[0]: item[1] for item in books}
# print(item_dict.items())
# lst = sorted(books.item())
# sorted=dict(lst)
books['Nikhil']= 500

sort = sorted(books.items())
lst = dict(sort)
print('lst is ', lst)