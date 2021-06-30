'''
#Alternate Solution

a,b = map(int,input().split())
available = 240 - b
z = []
x = []
total = 0
for i in range(1,a+1):
        z.append(i*5)
for j in range(len(z)):
    total += z[j]
    if total <= available:
        x.append(j)
    else:
        continue
print(len(x))
'''
n, k = list(map(int, input().split()))
solve = 0
for i in range(1, n+1):
    if k + (i * 5) <= 240:
        solve += 1
    k += (i * 5)
print(solve)
