x = input()
y = list(map(str,input().split()))
a = list(x)
for i in range(len(y)):
    j = list(y[i])
    if j[0] == a[0] or j[1] == a[1]:
        ans = 'YES'
        break
    else:
        ans = 'NO'
print(ans)



'''
Alternative solution...


a=input()
b=input()
for i in a:
    if i in b:
        print('YES')
	exit()
print('NO')
'''
'''
a = input()
b = list(map(str, input().split()))
flag = False
for i in b:
    if a[0] == i[0] or a[1] == i[1]:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
'''
