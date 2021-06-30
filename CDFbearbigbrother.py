x,y =  map(int, input().split())
count = 0
while count<y:
    if x % 10 == 0:
        x = x // 10
    else:
        x = x - 1
    count = count + 1
print(x)
    
'''
a,b = list(map(int,input().split()))
for i in range(b):
    if a % 10 == 0:
        a = a // 10
    else:
        a -= 1
print(a)'''
