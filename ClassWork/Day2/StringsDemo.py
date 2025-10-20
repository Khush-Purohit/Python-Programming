s4 = 'sit bit sit fit nit'
partition = s4.partition('sit')
print(partition)

t1 = (1,1,'Hello')
print(t1)

l1 = [1,'Hello']
l1.extend(t1)
print(l1)

words = ['pat','bat', 'rat', 'sat', 'fat','nik']
print(words)
lst = ['a','b','c','d','e','f']
print(lst[-6:-1:-1])
print(lst[-1:-6:-1])
print(lst[1:5:1])

lst.append('f')
print(lst)
lst.remove('b')
print(lst)

lst.append(['a','b','c'])
print(lst)
words1=[]
for item in lst:
    if not isinstance(item,list):
        words1.append(item);
    else:
        words1.extend(item)
print(words1)



