x = int(input())
count = 0
cubes = 1
adding = 2
total = 1
while total <= x:
    cubes += adding
    total += cubes
    count += 1
    adding += 1
print(count)


'''x = int(input())
z = []
z1 = []
for i in range(1,x):
    z.append(i)
    z1.append(i+1)
list1 = [1]
count = 0
a = 1
if x in range(1,3):
    print(a)
else:
    for i in range(len(z1)):
        b = z1[i]+list1[-1]
        nex = z1[i+1]
        last = x - sum(list1)
        if last >= nex:
            list1.append(b)
        else:
            print(len(list1))
            break'''
