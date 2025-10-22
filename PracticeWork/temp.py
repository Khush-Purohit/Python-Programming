# # lst = [1,2,5,32,1265,21,46,2562,43,4,5324,651234,245]

# # temp = [item for item in lst if item > 500]

# # print (temp)


# # squares = [i*i for i in lst ]
# # print(squares)


# # dict = {1:'one',
# #         2:'two',
# #          3:'three' }

# # new_dict = {i.value()+'hii' for i in dict}

# # print(new_dict)


# for _ in range(3):
#     print('Hello')  # This is inside the loop
# # print("Done")


# arr = [7, 3, 9, 1]
# d=9
# d = d%len(arr)
# arr.pop
# print(arr[d:] + arr[:d])


# st = {}
# st.




arr = [4, 3, 6, 2, 1, 1]
# print(arr)
# arr1 = []
# for i in range(0,len(arr)):
#     # print(arr[i])
#     for j in range(len(arr)-1):
#         arr1=arr[i]==arr[j]
# print(arr1)

# for i in range(0,len(arr)-1):
#     if arr[i]==arr[i+1]:
#         print(True)
#     # else:
#     #     print(False)
            



# print(arr)

# ans = []
# i=1
# n=len(arr)
# while(i <  n):
#     if (arr[i]==arr[i-1]):
#         if (len(ans)==0):
#             ans.append(arr[i])
#             i+=1
#             continue
        
#         elif(len(ans)>0):
#             # ans.
#             if (ans[-1] != arr[i]):
#                 ans.append(arr[i])        
        
#     i+=1


# arr = [4,3,6,2,1,1]

# # arr.sort()
# arr.sort() 
# ans=[]
# sum = arr[0]
# dup=0
# n = len(arr)
# for i in range(1,len(arr)):
#     sum+=arr[i]
#     if(arr[i] == arr[i-1]):
#         dup = arr[i]
#         ans.append(arr[i])

# sum = sum - dup
# print(f'sum is : {sum}')

# actual_sum = n*(n+1)//2

# print(f'actual sum is : {actual_sum}')


# print(ans)


# s = "5555..555"
# str=''
# for i in s:
#     if i!= '.':
#         str+=i
#     if i == '.':
#         num = int(str)
#         if(num)>=0 and 
# print(lst)

# s = '01.01.01.01'
# lst = s.split('.')


# if len(lst) != 4:
#     # return False
#     print('Not a valid ip')
# for i in lst:
    
#     if(i==''):
#         print('Not a valid ip')
#         # return False
#         break
        
#     else:
#         if (int(i)) >=0 and (int(i)) <=255:
#             continue
# # return True

# for i in lst:
#     if(i==''):
#         print('Not a valid ip')
#         break
        
#     else:
#         if (int(i)) >=0 and (int(i)) <=255:
#             continue

# print('valid ip')


# ####################################################################
# s = '19.132.268.45'

# lst = s.split('.')
        
# if len(lst) != 4:
#     print('False')
#     print('incorrect ip')
# print(lst)
# for i in lst:
#     print(int(i))
#     if(i==''):
#         print('False')
#         break
#     elif (i[0] == '0' and int(i) != 0):
#         print('False')
#         break
#     elif (int(i)) < 0 or (int(i)) > 255:
#         print('False')
#         break
# print('True')

def cmp(a,b):
    if(a[0] == b[0] and a[-1] == 0):
        return 

arr = [3, 30, 34, 5, 9]
expected = 9534330
for i in range(len(arr)):
    arr[i] = str(arr[i])

print(arr)

arr = sorted(arr, reverse = True)

print(arr)

s = ''

for i in arr:
    s += i

print(f'expected : {expected}')
print(f'current: {s}')