a= int(input())
for i in range(int(a)):
    n, x = list(map(int, input().split()))
    if n <= 2:
        print(1)
    else:
        n = n - 2
        if n % x == 0:
            ans = (n // x) + 1
        else:
            ans = (n // x) + 2
        print(ans)
        '''f = [2]
        while(f[-1] <= n):
            e = f[-1]+x
            f.append(e)
        q = f.index(f[-1])
        ans = len(f)
        if n % x == 0:
            ans = ans-1
            print(ans)
        else:
            print(ans)
        '''
