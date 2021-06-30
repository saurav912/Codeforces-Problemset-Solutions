x = int(input())
for i in range(x):
    a = int(input())
    list1 = []
    list2 = []
    z = []
    for j in range(1,a+1):
        z.append(2 ** j)
    z = sorted(z,reverse=True)
    f = len(z) // 2
    list1.append(z[0])
    z.remove(z[0])
    while len(list2) != f:
        for i in range(f):
            list2.append(z[i])        
        break
    for e in z:
        if e not in list2:
            list1.append(e)
    print(sum(list1) - sum(list2))

'''
ALTERNATIVE SOLUTION
1)
for i in range(int(input())):
    n=int(input())
    for i in range(n):
        res=(pow(2,(n//2+1))-2)
    print(res)

2)
user_input = int(input())
for i in range(user_input):
    coins = int(input())
    piles = []
    for j in range(1,coins+1):
        piles.append(2 ** j)
    temp = piles[(coins - 1) // 2 : coins - 1]
    print(sum(piles) - 2 * sum(temp))
'''
