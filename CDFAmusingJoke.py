a = input()
b = input()
c = input()
a = a + b
x = {}
y = {}
for i in a:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
for i in c:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
if x == y:
    print('YES')
else:
    print('NO')
        
