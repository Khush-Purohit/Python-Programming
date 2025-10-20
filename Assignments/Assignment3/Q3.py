print('Enter the list of words(to quit type "q"):')
lst = []
while(True):
    word = input("Enter word: ")
    if word == 'q':
        break
    lst.append(word)

d={}
def make_ing_form(lst, d):
    for i in lst:
        if(i[-2::] == 'ie'):
            d[i] = i[:-2:] + 'y' + 'ing'
        elif (i[-1] == 'e'):
            d[i] = i[:-1:] + 'ing'
make_ing_form(lst,d)
print(d)