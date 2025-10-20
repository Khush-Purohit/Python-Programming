#===========Question5==========
print('\n\n===========Question5==========')
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))

if(s1+s2>s3 and s2+s3>s1 and s3+s1>s2):
    print('Valid Triangle')

    if(s1 == s2 and s2 == s3):
        print('Equilateral Triangle')
    elif(s1 == s3 or s2 == s1 or s2 == s3):
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')

else:
    print('Invalid Triangle')