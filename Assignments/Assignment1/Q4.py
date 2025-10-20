#===========Question4==========
print('\n\n===========Question4==========')
num1 = int(input("Enter a 5 digit number"))
sum = 0
even = odd = digits =0
while(num1>0):
    if (num1%10%2==0):
        even+=1
    else:
        odd+=1
    sum=sum + num1%10
    digits+=1
    num1=num1//10
print('sum = ', sum)
print('evendigits = ', even)
print('odddigits = ', odd)
print('digits = ', digits)