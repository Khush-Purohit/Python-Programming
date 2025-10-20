#===========Question2==========
# print('\n\n===========Question2==========')
start=int(input("\n\nEnter start number: "))
end = int(input("Enter end number: "))

for i in range(start,end+1):
    isPrime = True
    for j in range(2,i):
        if(i%j==0):
            isPrime = False
            break
    if isPrime:
        print(i)



