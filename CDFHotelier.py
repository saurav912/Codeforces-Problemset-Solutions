n=int(input())
s=input()
l=['0']*10
for i in s:
	if i=="L":
		a=l.index('0')
		l[a]='1'
	elif i=='R':
		a=l[::-1].index('0')
		l[9-a]='1'
	else:
		l[int(i)]='0'
print(''.join(l))

'''
a = int(input())
b = input()
result = ['0'] * 10
for i in b:
    if i.isdigit():
        result[int(i)] = '0'
    elif i == 'L':
        for j in range(10):
            if result[j] != '1':
                result[j] = '1'
                break
    else:
        for j in range(9, -1, -1):
            if result[j] != '1':
                result[j] = '1'
                break
print(''.join(result))
'''
