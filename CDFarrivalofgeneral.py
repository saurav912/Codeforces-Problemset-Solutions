n = int(input())
a = list(map(int,input().split()))
x = min(a)
y = max(a)
count = a.index(y)
a.pop(count)
a.insert(0,count)
a.reverse()
ans = count + a.index(x)
print(ans)
