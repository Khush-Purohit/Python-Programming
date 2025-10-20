#===========Question3==========
print('\n\n===========Question3==========')
num1 = int(input("Enter a three digit number: "))
num2=0
while(num1>0):
    num2 = num2 * 10 + num1%10
    num1=num1//10

print(num2)