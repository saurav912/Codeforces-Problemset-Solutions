x,y = map(int,input().split())
count = 1
for i in range(x):
    if i % 2 != 0:
        if count == 1:
            z = '.'*(y-1) + '#'
            print(z)
            count = 2
        else:
            z = '#'+(y-1)*'.'
            print(z)
            count = 1
    else:
        print('#'*y)
    
'''
Alternative solution

n,m=list(map(int,input().split()))
for i in range(1,n+1):
    if i%2==1:
        print("#"*m)
    else:
        if i%4==0:
            print("#"+"."*(m-1))
        else:
            print("."*(m-1)+"#")
'''
