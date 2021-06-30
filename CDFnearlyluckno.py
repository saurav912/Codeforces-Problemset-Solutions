x = int(input())
y = []
x = list(map(int, str(x)))
count = 0
for i in range(len(x)):
    if x[i] == 4 or x[i] == 7:
        y.append(i)
        count = count + 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')
