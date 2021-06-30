x = int(input())
for i in range(x):
    a,b,c = map(int,input().split())
    f = c - b
    g = (f % a)
    ans = c - g
    print(ans)
    
'''
Alternate logic...
z = c % a;
    if(z >= b):
        print(c - (z - b))
    else:
        print(c - (z + a - b))
        '''
