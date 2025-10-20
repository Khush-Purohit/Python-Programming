print('Enter the list of words(to quit type "q"):')
lst = []
while(True):
    word = input("Enter word: ")
    if word == 'q':
        break
    lst.append(word)

print(lst)
max_word = ''
for i in lst:
    if(len(i)>len(max_word)):
        max_word = i

print(f'the longest word is: {max_word}')