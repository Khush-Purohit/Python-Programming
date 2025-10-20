from functools import reduce


numbers = [1,4,5,6,10,13,14,5,4,3,7,89,54]

def calculate_squares(n):
    return n*n

squares = list(map(calculate_squares, numbers))
# squares = (map(calculate_squares, numbers))

squares = list(map(lambda num : num*num , numbers))
print(squares)


even = list(filter(lambda n:n%2==0, numbers))
print(even)


min_num = reduce (lambda n1,n2:n1 if n1<n2 else n2 , numbers )
print(min_num)


