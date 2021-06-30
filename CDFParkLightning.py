x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    c = a*b
    ans = c//2 + c%2
    print(ans)
