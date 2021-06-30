a = int(input())
for i in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    c = list(set(c))
    g = []
    h = [-1,0,1]
    for i in range(len(c)-1):
        g.append(c[i]-c[i+1])
    for i in g:
        if i not in h:
            print('NO')
            continue
        else:
            print('YES')
