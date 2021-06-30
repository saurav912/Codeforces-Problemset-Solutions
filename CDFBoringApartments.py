x = int(input())
for i in range(x):
    a = int(input())
    c = len(list(map(int,str(a))))
    b = [1,2,3,4]
    p = a % 10
    ans = ((p-1)*10)+sum(b[:c])
    print(ans)

