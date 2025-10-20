lst = input("Enter a list of words separated with comma(,): ")
lst = lst.split(',')
print(lst)
maxWord = ''
maxLen = 0
for word in lst:
    if(len(word) > maxLen):
        maxLen = len(word)
        maxWord = word
print("Longest word is :", maxWord)
print("Longest word length is :", maxLen)
