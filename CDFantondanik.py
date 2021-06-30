x = input()
a = list(input())
if a.count('D')>a.count('A'):
    print('Danik')
elif a.count('D')<a.count('A'):
    print('Anton')
else:
    print('Friendship')
