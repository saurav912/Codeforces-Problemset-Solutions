x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    if (a == 1):
        print(0)
    elif (a == 2):
        print(b)
    else:
        print(2 * b)
