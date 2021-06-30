x = int(input())
for i in range(x):
    a, b = list(map(int, input().split()))
    result = b - a
    d = result % 2
    if result > 0:
        if d == 0:
            print(2)
        else:
            print(1)
    elif result < 0:
        if d == 0:
            print(1)
        else:
            print(2)
    else:
        print(0)

'''
for i in range(int(input())):
    a, b = list(map(int, input().split()))
    result = b - a
    answer = 2
    if result > 0 and result % 2 != 0:
        answer = 1
    elif result < 0 and result % 2 == 0:
        answer = 1
    elif result == 0:
        answer = 0
    print(answer)
'''
