x = int(input())
z = [1,5,10,20,100]
a = x
count = 0
while x>0:
    if x >= max(z):
        b = x // max(z)
        count += b
        x = x-(max(z)*b)
    else:
        z.remove(max(z))
print(count)

'''
a = int(input())
b = [100, 20, 10, 5, 1]
total = 0
for i in b:
    temp = a % i
    temp1 = a // i
    if temp == 0:
        total += temp1
        break
    else:
        total += temp1
        a = temp
print(total)
'''
        

