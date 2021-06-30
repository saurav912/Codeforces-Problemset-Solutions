n,k=list(map(int,input().split()))
m=list(map(int,input().split()))
count=0
temp=m[k-1]
for i in m:
    if i>=temp and i>0:
        count+=1
print(count)        
