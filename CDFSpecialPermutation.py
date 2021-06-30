x = int(input())
for i in range(x):
    a = int(input())
    z = []
    for i in range(1,a+1):
        z.append(i)
    z = z[::-1]
    if a % 2 == 0:
        b = z
        print(*b)
    else:
        mid = len(z)//2
        z[mid],z[mid+1] = z[mid+1],z[mid]
        b = z
        print(*b)
        
