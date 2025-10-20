word = input("Enter a sentence: ")
rev_word = word[::-1]
isP = True
for i in range(len(word)):
    if(word[i].isalpha() and rev_word[i].isalpha()):
        if word[i] == rev_word[i]:
            continue
        else:
            print("this is not a pallindrome")
            isP = False
            break
if isP:
    print("This is a pallindrome")