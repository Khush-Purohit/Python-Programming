# def increment(n):
#     return n+1

# # function assigned to a variable
# inc = increment

# # variable can be used in case of the function
# print(inc(20))

# # Anonymous function
# inc = lambda n:n+1
# print(inc(30))

# l0 = lambda :100
# print(l0())

# l1 = lambda n1,n2,n3=6:n1+n2+n3
# print(l1(1,2))


# my_list = [1,2,3,4]
# l2 = lambda *args:sum(args)
# print(l2(1,2,3,4,5,5,6))
# print(l2(*my_list))


values = {'data':[1,2,3,4]}
l3 = lambda **kwargs :sum(kwargs.values())
print(l3(one=1,two=2, three=3))
# print(l3(**data))