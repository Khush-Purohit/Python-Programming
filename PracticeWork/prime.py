num = int(input("Enter a number: "))
isPrime = True
for i in range(2,num):
    if num % i == 0:
        isPrime = False
        break
else:
    print("This is a prime number")
if isPrime:
    print("The number is prime")