a = int(input())
x = list(map(int, input().split()[1:]))
y = list(map(int, input().split()[1:]))
total = sorted(list(set(x+y)))
if list(range(1, a+1)) == total:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
