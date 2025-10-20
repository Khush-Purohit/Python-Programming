# # # # This is a sample Python script.
# # #
# # # # Press Shift+F10 to execute it or replace it with your code.
# # # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # #
# # #
# # # def print_hi(name):
# # #     # Use a breakpoint in the code line below to debug your script.
# # #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # #
# # #
# # # # Press the green button in the gutter to run the script.
# # # if __name__ == '__main__':
# # #     print_hi('PyCharm')
# # #
# # # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #
# #
# # i=10
# # print(i)
# # print(type(i))
# # print(id(i))
# #
# # j=10
# # print(i==j)
# # print (i is j)
# #
# # k = 23.3
# # print(k)
# # print(type(k))
# # print(id(k))
# #
# #
# #
# #
# #
# # a=10
# # b=24.5
# #
# # print(float(a))
# # print(int(b))
# #
# # # name = (input("Enter your name : "))
# # # age = int(input("Enter your age : "))
# #
# #
# # val=4e-5
# # print(val)
# # print(f"{val:.8f}")
# #
# # # print('You have entered: ',name, 'and age is : ', age)
# from xmlrpc.client import boolean
#
# # for i in range(1,11,2):
# #     if i==5:
# #         continue
# #     print(i)
# #
# #
# # st = 'this is a string'
# #
# # for ch in st:
# #     print(ch)
#
#
# # num = int(input("Enter a number: "))
# # isPrime = True
# # for i in range(2,num):
# #     if num % i == 0:
# #         isPrime =False
# #         break;
# # else:
# #     print("This is a prime number")
# # if isPrime:
# # if isPrime:
# #     print("The number is prime.")
#
#
# i=0
# while(i<10):
#     i+=1
#     if(i==5):
#        continue
#     print(i)
#
#
#
# num=int(input("Enter a number:"))
# i=2
# while(i<num):
#     if num%i==0:
#         print('number is not prime')
#         break
#     i+=1
# else:
#     print('number is prime')
#
#
#
#

# n=153
# temp = n
# arm = 0
# while (n):
#     num = n % 10
#     arm += num * num * num
#     n = n // 10
# print(arm)

import string
s1='1234'
s1 = 'helloA'
print(s1.isalnum())
print(s1.isdecimal())


s1 = '12\u00B2\u000B3'
print(s1)
print(s1.isnumeric())



s2 = 'Welcome to Python'
print(s2.lower())
print(s2.upper())
print(s2.title())
print(s2.capitalize())
print(s2.swapcase())



#==other methods

s3 = 'sit bit fit chit'
words = s3.split(' ')#mostly used with comma separated files
print(words)
print(s3.count('sit'))



