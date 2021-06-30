for i in range(int(input())):
    a = list(map(int, input().split()))
    total = sum(a) % 3
    answer = sum(a) // 3
    if total == 0:
        maximum = max(a[:-1])
        if maximum <= answer:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
