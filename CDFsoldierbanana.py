x,y,z =  map(int, input().split())
list1 = []
a = 0
for i in range(z+1):
    a = x*i
    list1.append(a)
if sum(list1) <= y:
    print(0)
else:
    print(sum(list1)-y)
