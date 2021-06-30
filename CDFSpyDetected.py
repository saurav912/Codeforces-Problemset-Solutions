x = int(input())
for i in range(x):
    y = int(input())
    z = list(map(int,input().split()))
    z1 = list(set(z))
    count1 = z.count(z1[0])
    count2 = z.count(z1[1])
    if count1 < count2:
        pos = z.index(z1[0])
        print(pos+1)
    else:
        pos = z.index(z1[1])
        print(pos+1)
