x,y = map(int,input().split())
z = list(map(int,input().split()))
count = 0
for j in range(len(z)):
    if z[j] + y <= 5:
        count += 1
ans = count//3
print(ans)


'''x,y = map(int,input().split())
z = list(map(int,input().split()))
triplet = []
count = 0
for i in z:
    if i <= 1:
        triplet.append(i)
        triplet.sort()
count += len(triplet)//3
print(count)'''
