arr = [12, 35, 1, 10, 34, 1]


max1 = 0

# for i in range(len(arr)):
#     if arr[i]>max1:
#         max1 = arr[i]


st = set(arr)

for i in st:
    if max1 < i:
        max1 = i

st.remove(max1)

# if len(st) == 0:
#     return -1
print(max(st))