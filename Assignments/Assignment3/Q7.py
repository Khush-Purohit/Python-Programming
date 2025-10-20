#min,max,avg

weather= [{'Mumbai' : [28, 30, 32]},
         {'Pune':[24,34,28]},
         {'Nashik':[20,38,25]}]

#==========Q1==========
print(weather)

#==========Q2==========
min_max = list(map(lambda item: [next(iter(item)), list(item.values())[0][0], list(item.values())[0][1]], weather))
print(min_max)

#==========Q3==========
filtered = list(filter(lambda item: list(item.values())[0][0] > 30, weather))
print(filtered)


#==========Q4==========
dict_new = {}

for i in weather:
    k = i.keys()
    for j in k:
        dict_new[j] = i.get(j)[2]

print(dict_new)