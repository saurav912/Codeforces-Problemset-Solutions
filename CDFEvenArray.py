t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    k=0
    for i in range(n):
        if a[i]%2!=0:
            k+=1    
        if a[i]%2!=0 and i %2==0:
            m+=1
    if(n//2!=k):
         print(-1)   
    else:
         print(m)
            
