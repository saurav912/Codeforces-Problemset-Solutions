x = int(input())
for i in range(x):
    a,b,c = sorted(map(int,input().split()))
    if b == c:
        print('YES')
        print(a,a,c)
    else:
        print('NO')
        

'''
for i in range(int(input())):
    a = list(map(int, input().split()))
    temp = list(set(a))
    if len(temp) < len(a):
        count = a.count(max(temp))
        if count > 1:
            print('YES')
            if len(temp) == 1:
                print(temp[0], temp[0], temp[0])
            else:
                print(*temp,1)
        else:
            print('NO')
    else:
        print('NO')
'''
