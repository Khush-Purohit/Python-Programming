#==========Q1==========
emp = {'Amol' : ['C', 'C++','Java'], 'Nikhil':['C', 'Python','SQL']}

for k,v in emp.items():
    print(k,' ',v)

#==========Q2==========
print('\nEmployees who know java are :')
for k,v in emp.items():
    if 'Java' in v:
        print(k,' ',v)

#==========Q3==========
emp['Amol']=['Tableau']
emp['Nikhil'] = ['God of war']
print('\nUpdate employees are:')
for k,v in emp.items():
    print(k,' ',v)
#==========Q4==========
emp['Khush'] = ['Java', 'cpp','Visualization']
emp.pop('Amol')

print('\nafter removing :')
for k,v in emp.items():
    print(k,' ',v)