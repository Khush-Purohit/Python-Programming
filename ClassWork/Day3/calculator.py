import math
import math as m
from math import multiply
from math import division as d
ch = int(input(print('Enter your choice: 1.Addition 2. Subtraction 3.multiplication 4.Division')))

num1 = int(input('Enter first no'))
num2 = int(input('Enter second no'))
match ch:
    case 1:
        result = math.add(num1,num2)
        print(result)
    case 2:
        result = m.subtract(num1,num2)
        print(result)

    case 3:
        result = multiply(num1,num2)
        print(result)

    case 4:
        result = d(num1,num2)
        print(result)