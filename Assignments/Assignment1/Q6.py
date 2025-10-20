#===========Question6==========
print('\n\n===========Question6==========')
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

#LCM
lcm = 1
great = max(num1, num2)

while True:
    if(great%num1==0 and great%num2==0):
        print("The LCM number is",great)
        break
    great = great + 1


#HCF
i = hcf =1
smaller = min(num1, num2)
while(i <= smaller):
    if(num1%i==0 and num2%i==0) :
        hcf=i
    i+=1
print('hcf is : ',hcf)