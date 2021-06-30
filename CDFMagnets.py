'''from itertools import groupby

a = int(input())
j = []
for i in range(a):
    b = int(input())
    j.append(b)
res = [list(y) for x, y in groupby(j)]
print(len(res))'''
a = int(input())
group_number = 0
group = None
for i in range(a):
    b = int(input())
    if group == None :
        group = b
        group_number += 1
    else:
        if b != group:
            group_number += 1
            group = b
print(group_number)
        
        
