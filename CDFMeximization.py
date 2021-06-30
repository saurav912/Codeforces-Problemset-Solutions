x = int(input())
for i in range(x):
    y = int(input())
    z = list(map(int,input().split()))
    f1 = []
    f2 = []
    for i in z:
        if i not in f2:
            f2.append(i)
        else:
            f1.append(i)
    ans = sorted(f2)
    ans.extend(f1)
    print(*ans)

'''
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b = sorted(list(set(a)))
    for i in b:
        a.remove(i)
    print(*(b+a))
'''
