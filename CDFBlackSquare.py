'''x = list(map(int,input().split()))  
y = list(map(int,str(int(input()))))
ans = 0
for i in y:
    ans = ans + x[i-1]
print(ans)
'''
a = list(map(int, input().split()))
b = input()
result = 0
for i in b:
    result = result + a[int(i) - 1]
print(result)
