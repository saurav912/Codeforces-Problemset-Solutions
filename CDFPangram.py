x = int(input())
y = input()
y = y.upper()
y = list(y)
if len(set(y)) == 26:
    print('YES')
else:
    print('NO')
