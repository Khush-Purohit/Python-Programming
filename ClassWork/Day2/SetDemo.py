st = {'banbana', 'apple'}
print(st)
st.add('abab')
print(st)

# print(st.remove('cc'))


st.update({'letchi', 'banana'})
print(st)

k = st.union({'java'})
print(k)




s1 = {'pune', 'nasik', 'bombay', 'nagpur'}
s2 = {'indore', 'delhi', 'nagpur', 'nasik'}

s1_s2 = s1.intersection(s2)
print(s1_s2)

print(s1)
s1.pop()
print(s1)


print(s1 | s2 , "union set")
print(s1 & s2 , "intersection set")


