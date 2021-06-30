a,b = map(int,input().split())
x,y = 0,0
minimum = min(a,b)
if minimum == a:
    x = a
    y = (b-a)//2
elif minimum == a and minimum == b:
    x = a
    y = 0
else:
    x = b
    y = (a-b)//2
print(x,end = " ")
print(y)

'''
a, b = list(map(int, input().split()))
different = min(a, b)
same = max(a, b) - different
same = same // 2
print(different, same)
'''
