emp_data = {'Amol': ['C', 'C++', 'Java'], 
            'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

#==========q1==========
for k,v in emp_data.items():
    if 'python' in v:
        print(k, ' ', v)


#==========q2==========
for k,v in emp_data.items():
    v.append('test')
for k,v in emp_data.items():
    print(k, ' ', v)


#==========q3==========
lst = list(emp_data.items())
temp = sorted(lst,key = lambda item:len(item[1]) , reverse=True)
print(temp)