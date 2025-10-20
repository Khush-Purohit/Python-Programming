#Decorator
def smart_math(inner):
    def wrapper(*args):
        n1,n2=args
        if n1<n2:
            n1,n2 = n2,n1
        return inner(n1,n2)
    return wrapper

@smart_math
def subtract(num1,num2):
    return num1 - num2

print(subtract(23,12))
print(subtract(3,22))


