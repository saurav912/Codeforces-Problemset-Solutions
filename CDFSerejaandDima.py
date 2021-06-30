x = int(input())
a = list(map(int, input().split()))
sereja = 0
dima = 0
for i in range(x):
    maximum = max(a[0], a[-1])
    if i % 2 == 0:
        sereja += maximum
        a.remove(maximum)
    else:
        dima += maximum
        a.remove(maximum)
print(sereja, dima)


    
