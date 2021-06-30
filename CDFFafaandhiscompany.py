a = int(input())
count = 0
for i in range(1, (a // 2) + 1):
    if (a - i) % i == 0 :
        count += 1
print(count)

'''
ALTERNATE SOLUTIONS:

a = int(input())
count = 0
x = a // 2
z=[]
for i in range(1,a+1):
    z.append(i)
for i in z:
    if (a - i)%i == 0:
        count += 1
print(count-1)


n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(n)
print(len(l))
'''
