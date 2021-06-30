x = int(input())
y = list(map(int,input().split()))
largest = max(y)
add = 0
for i in range(len(y)):
    add += int(largest - y[i]) 
print(add)

'''
x = int(input())
y = sorted(list(map(int,input().split())))
largest = y[-1]
y.remove(largest)
add = 0
for i in range(len(y)):
    add += int(largest - y[i]) 
print(add)
'''
