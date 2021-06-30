for i in range(int(input())):
    a = int(input())
    b = list(map(str, input().split()))
    result = []
    for j in b:
        if j not in result:
            result.append(j)
    print(' '.join(result))
