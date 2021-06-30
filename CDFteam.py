x = int(input())
count = 0
for i in range(x):
    n = list(map(int,input().split()))
    num = 1
    if n.count(num)>=2:
        count = count + 1
print(count)
            
