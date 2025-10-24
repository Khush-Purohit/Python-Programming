# my_tuple = (10,20,30)

# print(my_tuple)

# print(my_tuple[1])

# print(my_tuple[1:])

# print(len(my_tuple))

# nested = ((1,2), (3,4))
# print(nested)
# print(nested[1][0])


# t1 = (1, 2, 3, 4)
# t2 = (5, 6, 7, 8)
# t3 = t1 + t2
# print(t3)


# print(t1*3)


# mixed_tuple = (1, 'apple' , 2, 3, 'ball')
# print('apple' in mixed_tuple)


# for item in my_tuple:
#     print(item)




# # create a tuple with five numbers. print the second and fourth elements

# num = (1, 2, 3, 4, 5)
# print(num[1::2])


# #Write a function that takes a tuple of numbers and returns a new tuple with only the even numbers

# def even_no(tuple_n):
#     even_numbers = []
#     for i in tuple_n:
#         if(i%2==0):
#             even_numbers.append(i)
#     return tuple(even_numbers)

# tuple_n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# New_tuple = even_no(tuple_n)
# print(New_tuple)


# ############# List Comprehension ############


# def even_nos(tuple_n):
#     return tuple(i for i in tuple_n if i % 2 == 0)


# print(even_nos(tuple_n))



########################### Dictionary ############################

# student = {
#     'name' : 'Alice',
#     'age' : 21,
#     'courses' : ['Math', 'Science']
# }

# print(student['name'])

# print(student.get('grades', 'Not Found'))

# student['age'] = 22
# student['grade'] = 'A'
# print(student)

# del student['courses']
# print(student)

# # for key, value in student.items():
# #     print(key, " : ", value)

# for k , v in student.items():
#     print(k ,':', v)


# print(student.get('name', 'Not Found'))

# print(student.keys())

# print(student.values())

# print(student.items())

# print(student.update({'course': 'DBDA'}))
# print(student)

# student.pop('age')
# print(student)


# print()
# print('############### Dictionary Comprehension ########\n')

# sq = {x: x*x for x in range(1,6)}
# print(sq)

# #Create a dictionary with three students and their scores. Print the score of one student.
# stud = {
#     'stud_1' :{'name': 'alice', 'score':98},
#     'stud_2' :{'name': 'blice', 'score': 99},
#     'stud_3' :{'name': 'clice', 'score': 100}
# }

# print(stud['stud_1']['score'])


# #Write a function that takes a dictionary of items and prices, and returns a list of items priced above ₹100.
# def items(dictionary_items):
#     return list[{k:v['price'] for k,v in dictionary_items.items() if v['price']>100}]


# dictionary_items = {
#     'apple': {'price':200},
#     'banana': {'price':60},
#     'blueberry': {'price':350},
#     'orange' : {'price':150}
# }

# print(items(dictionary_items))


################# Functions ####################


# def addition(num1, num2):
#     return num1+num2

# print(addition(10,20))


# def greet(name):
#     print(f'Hello, {name}')

# greet('Nikhil')


# ######### No arguments, no return ##########
# def say_hello():
#     print('Hi')

# say_hello()

# ################ with arguments ###################

# def square(x): 
#     return x*x

# print(square(5))


# ############# with default arguments #############

# def greet(name):
#     return name

# print(greet(name='alice'))


# ############### with variable arguments ##############

# def total(*nums):
#     return sum(nums)

# print(total(1,2,3,4))



# #Write a function that takes a number and returns its factorial.

# def fact(num):
#     factorial = 1
#     for i in range(1,num+1):
#         factorial = factorial*i
#     return factorial

# print(fact(5))

# #Write a function that accepts a list of numbers and returns the maximum value.

# def maximum(*nums):
#     return max(nums)

# print(maximum(1,10,4,5))



# #Write a function that takes any number of numbers and returns their average. Use *args.
# import statistics
# def avg(*args):
#     # total = sum(args)
#     # count = len(args)
#     # return total/count
#     return statistics.mean(args)

# print(avg(1,2,3))



# #Write a function that accepts any number of keyword arguments and prints them in the format key = value. Use **kwargs

# def format(**kwargs):
#     # for k,v in kwargs.items():
#     # print(f"{k}: {v}")
#     print("keywords: ", kwargs)

# new_format = format(age=25, city='pune')
# print(new_format)



############# Lambda #################

# square = lambda x: x*x
# print(square(10))

# addition = lambda num1, num2: num1+num2
# print(addition(1,2))

# nums = [1,2,3,4]
# square = list(map(lambda x: x**2, nums))
# print(square)

# even = list(map(lambda x: x%2 == 0, nums))
# print(even)

# nums1 = [10,20,15,40,65,60]
# even_no = list(filter(lambda x: x%2 == 0, nums1))
# print(even_no)

# students = [("Ravi", 85),("priya",92),("Amit",78)]
# sorted_students = sorted(students,key=lambda x: x[1])
# print(sorted_students)      


# #Use a lambda function with map() to convert a list of temperatures in Celsius to Fahrenheit.

# #(°C × 9/5) + 32 = °F

# temp = [1,2,15,35]
# Fahrenheit = list(map(lambda x: (x * 9/5) + 32,temp))
# print(Fahrenheit)


# #Use a lambda with filter() to extract words longer than 5 characters from a list.

# char = ['alice','ravi','nikhil','sumesh','tejas']

# more_than_5_char = list(filter(lambda x: len(x)>5,char))
# print(more_than_5_char)




################ Strings #################


# text = "Python,is fun!"

# print(len(text))

# print(text[1])

# print(text[0:6])

# print("Hello " + "World")

# print("hi " * 3)


# print(text.lower())
# print(text.upper())
# print(text.strip())
# print(text.replace('fun','easy'))
# print(text.split(','))
# print(text.join(['aviram', 'ishaan']))
# print(text.find('is'))
# print(text.count('is'))


# msg = " hello world "
# print(msg.strip().upper())


# name = 'alice'
# age = 25

# print(f'my name is {name} and i am {age} years old')



# #Write a function that takes a string and returns the number of vowels in it.


# def vowels(string):
#     vow = []
#     for i in string:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#             vow.append(i)
#     return vow
# string = 'python'
# print(vowels(string))


# #Write a function that reverses a string and checks if it’s a palindrome.

# str = 'Sore was I ere I saw Eros.'

# def is_palindorm(str):
#     reverse = string[::-1]
#     return string == reverse
# print(is_palindorm('toy'))




################ Class #####################

class person:
    
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"my name is {self.name} and my age is {self.age} year old")


p1 = person("ravi", 21)
p1.greet()