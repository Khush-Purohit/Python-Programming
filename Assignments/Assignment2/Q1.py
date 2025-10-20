st = input("Enter a string: ")
allUpper = True
for ch in st:
    if ch>='A' and ch<='Z':
        continue
    else:
        print("Word contains lower case alphabets")
        allUpper = False
        break
if allUpper:
    print("Word contains uppercase only")