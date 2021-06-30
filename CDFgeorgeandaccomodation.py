x = int(input())
count = 0
for i in range(x):
    a,b = map(int,input().split())
    if (b - a)>=2:
        count = count + 1
print(count)
