def primenumber(value):
    last = value // 2
    for i in range(2, last+1):
        if value % i == 0:
            return False
    return True
user_input = int(input())
subtraction = 4
while True:
    temp = user_input - subtraction
    temp1 = primenumber(temp)
    if temp1 == True:
        subtraction += 2
    else:
        print(subtraction, temp)
        break

'''Alternate solution
n=int(input())
a=n%2+8
print(a,n-a)
a=n%2*5+4
'''
