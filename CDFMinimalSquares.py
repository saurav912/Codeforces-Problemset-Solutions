x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = min(a,b)
    d = max(a,b)
    f = 0
    w = 2 * c
    if w > d:
        f = d + (w - d)
    elif w < d:
        f = w + (d - w)
    else:
        f = d
    print(f*f)
