for i in range(int(input())):
    x = int(input())
    result = [1]
    for i in range(x-1):
        m = result[-1]*3
        y = [int(i) for i in str(m)]
        if len(y) > 3:
            m = 999
        result.append(m)
    print(*result)
