x,y = map(int,input().split())
a = [0,1,2,3,4,5,6,7,8,9]
b = []
z = []
for i in a:
    b.append(x*i)
for i in range(1,len(b)):
    if b[i] % 10 == y or b[i] % 10 == 0:
        #print(b[i])
        #ans = b[i]//(10+y)
        z.append(b.index(b[i]))
print(min(z))

'''
Alternate solution (i).........using string

a, b = list(map(str, input().split()))
result = a
i = 1
while True:
    if result[-1] == b or result[-1] == '0':
        break
    else:
        i += 1
        result = str(int(result) + int(a))

print(i)

Alternate solution(ii).........using while loop
a, b = list(map(int, input().split()))
i = 1
while True:
    temp = a * i
    if temp % 10 == 0 or temp % 10 == b:
        print(i)
        break
    else:
        i += 1

'''
