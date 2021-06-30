z = int(input())
for i in range(z):
    x = int(input())
    a = x % 2
    b = x // 2
    if a == 0 and x > 2:
        print(b-1)
    elif a != 0:
        print(b)
    else:
        print(0)
        
