a,b,c = map(int,input().split())
z = [a,b,c]
z = sorted(z)
p = z[1]-z[0]
q = z[2] - z[1]
print(p+q)
