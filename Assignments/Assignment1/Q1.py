#===========Question1==========
print('\n\n===========Question1==========')
n=int(input("Enter a number: "))

for i in range(n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)
# print(fact)