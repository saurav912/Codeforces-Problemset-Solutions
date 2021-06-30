for i in range(int(input())) :
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    p=[]
    for i in range(len(a)-1) :
        p.append(abs(a[i+1]-a[i]))
    print(min(p))

'''timetaken := 77ms'''
'''x = int(input())
for i in range(x):
    y = int(input())
    z = sorted(list(map(int,input().split())))
    if len(set(z)) == len(z):
        list1 = []
        list2 = []
        for j in range(len(z)):
            for n in range(len(z)):
                list1.append(z[n] - z[j])
        for num in range(len(list1)):
            if list1[num] > 0:
                list2.append(list1[num])
        ans = min(list2)
    else:
        ans = 0
    print(ans)
'''
'''TimeTaken := 1278ms'''
