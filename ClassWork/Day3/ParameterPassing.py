def inc(n):
    n+=1
    return n
num=10
inc(num)
print(num)
incremented = inc(10)
print(incremented)

def inc_lst(lst):
    lst[0]+=1

lst = [1]
print(lst)
inc_lst(lst)
print(lst)