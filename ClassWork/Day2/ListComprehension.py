# nums = [1,2,3,4,5,6,7,8,9,10]
#
# sq=[]
#
# for i in nums:
#     sq.append(i*i)
#
# print(sq)
#
# sq= [num*num for num in nums]
# print(sq)
#
# #list unpacking..
# books = [['Python for beginners', 500], ['Blackbook for java',900],['java for dummies',1000] ]
# for title,price in books:
#     print(title,price)
#
#
# for index,value in enumerate(nums):
#     print(index,'.',value)
#
#
from idlelib.pyshell import usage_msg
#
# words = ['pat', 'bat', 'mat', 'rat', 'sat', 'fat']
#
# print(words[5])
# print(words[-5])
# words.append('khu')
# print(words)
# words.remove('khu')
# print(words)
# words.append(['sat','cat'])
# print(words)
# words.extend(['sat','bat'])
# print(words)
# words.pop(3)
# print(words)
#
#
#
# words1 = []
# for item in words:
#     if not isinstance(item,str):
#         words1.append(item)
#     else:
#         words.extend(item)
# print(words1)
# words1.sort()
# print(words1)



nums = [1,2,3,4,5,7,8,9]
price = [780,560,550,400,340,300,200]

# 2 usages
def calculate_discount(price):
    return price * 0.8

sq = []
for num in nums:
    sq.append(num * num)
print(sq)

sq = [calculate_discount(price[1]) for num in nums]
print(sq)


cards = ('spades', 'diamonds', 'hearts', 'clubs')

print('spades' not in cards)

for item in cards:
    print(item)

one,two,three,four = cards

print(one)
print(two)
print(three)
print(four)

l_cards = list(cards)
l_cards.append('spades')
cards = (tuple)(l_cards)
print(cards)


t1 = (1,2,3,4,5)
t2 = ('one','two','three','four')
t3 = tuple(zip(t1,t2))
print(t3)


sq = [n*n for n in t1]
print(sq)