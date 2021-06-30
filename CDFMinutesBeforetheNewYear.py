x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    a = a*60
    time = a + b
    rem = 1440 - time
    print(rem)
