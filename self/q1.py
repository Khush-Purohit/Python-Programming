path = input("Enter path: ")

# # count = {
#     'N' : 0,
#     'S' : 0,
#     'E' : 0,
#     'W' : 0
# }
# i=0
def isNW(a,b):
    if (a=='N' and b == 'S') or (b=='N' and a == 'S'):
        return True
    return False 

def isEW(a,b):
    if (a=='E' and b == 'W') or (b=='E' and a == 'W'):
        return True
    return False 
moves_ret = 0
for i in range(1, len(path)) :
    if(isNW(path[i], path[i-1]) or isEW(path[i], path[i-1])):
        moves_ret+=1

print(f"ROBOT COMMAND LOG: {path}")
print(f"TOTAL COMMANDS: {len(path)}")
print(f"RETURN MOVES DETECTED: {moves_ret}")

if(len(path)>=5 and moves_ret<2):
    print('PATH IS EFFICIENT! FINAL PATH ANALYSIS COMPLETE')
else:
    print('Path is NOT EFFICIENT')