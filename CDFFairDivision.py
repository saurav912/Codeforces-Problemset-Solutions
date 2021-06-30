for i in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    x = m.count(1)
    y = m.count(2)
    if (x%2==0 and (y%2==0 or x>=2)):
        print("YES")
    else:
        print("NO")
