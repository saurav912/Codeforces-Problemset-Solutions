x = int(input())
a = 0
for i in range(0,x):
    b = input()
    if b == 'X++' or b == '++X':
        a = a + 1
    elif b == 'X--' or b == '--X':
        a = a - 1
print(a)
