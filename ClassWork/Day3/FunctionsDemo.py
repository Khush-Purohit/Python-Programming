def simple_function():
    print('this is a simple function')

def addition(num1:int,num2:int):
    return num1+num2

result = addition(12,23)
print(result)

result = addition(12.23,23.23)
print(result)

result = addition([12,78],[23,12])
print(result)

result = addition((12,23),(23,23))
print(result)

def calculate_discount(product='table',price=5000):
    print(f'Discounted price for {product} is {price*0.8}')

# calculate_discount(900,'book')


'''positional arguments'''

calculate_discount(price=900,product='book')

calculate_discount()
calculate_discount('chair')
calculate_discount(price=1000)

'''varicable arguments
variable keyword arguments'''

def add(*nums):
    total=0
    for num in nums:
        total+=num
    print(total)
    print(type(nums))
add(23,23,213,55436,4365,2,324,143)

numbers = [1,2,3,4,4,326,265,345,511,45]

# add(numbers)
add(*numbers)

def calculate_average(**kwargs):
    print(type(kwargs))
    numbers = kwargs('Nums')
    total=0
    for number in numbers:
        total+=number
    return total/len(values)

calculate_average()



student = {
    'name':'prr',
    'marks':[90,89,78,89]
}

