x = int(input())
a = []
b = 1
y = [1]
z = []
for i in range(x):
    a.append(b)
    if i > 0:
        y.append(a[i]+i)
for k in range(x-2):
    for k in range(len(y)):
        if k == 0:
            z.append(y[0])
        else:
            z.append(z[k-1]+y[k])
    y = z
    z = []
print(max(y))

'''
a = int(input())
result = []
for i in range(a):
    result.append([1] * a)
for i in range(1, a):
    for j in range(1, a):
        result[i][j] = result[i - 1][j] + result[i][j - 1]
print(result[a-1][a-1])
'''
