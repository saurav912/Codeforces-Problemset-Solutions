n, m = list(map(int,input().split()))
z = True
for i in range(n):
    a = list(map(str,input().split()))
    list1 = ['C','M','Y']
    for j in list1:
        if j in a:
            z = False 
if z:
    print('#Black&White')
else:
    print('#Color')
