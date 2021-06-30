'''x = int(input())
for i in range(x):
    a = int(input())
    count = 0
    list1 = []
    k = []
    for i in range(1,a+1):
        list1.append(i)
    for j in list1:
        f = [int(d) for d in str(j)]
        if len(set(f)) == 1:
            count += 1  
    print(count)
'''
x = int(input())
for i in range(x):
    n = int(input())
    length = len(str(n)) # Length of digit of n
    a = 9*(length-1) 
    k = "1"*length # For N in range 1-9 , 11-99, 111-999..(no's will be only divisible by len(digits)*1)
    b = n//(int(k))
    ans = a + b
    print(ans)
    
