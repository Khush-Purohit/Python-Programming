print('Enter two lists of same size')

lst1 = list(input("Enter a first list in contiguous manner: "))
lst2 = list(input("Enter a second list in contiguous manner: "))

print(lst1)
print(lst2)

def overlap(lst1, lst2):
    #using list comprehension
    lst3 = [lst1[i]==lst2[i] for i in range(len(lst1))]

    for i in lst3:
        if i==True:
            return True
    return False

print(overlap(lst1,lst2))