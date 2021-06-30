x = int(input())
for i in range(x):
    a = list(input())
    if len(a)==2:
        print("".join(a))
    else:
        b = []
        for z in range(1):
            b.append(a[z])
        for j in range(2,len(a),2):
            b.append(a[j])
        b.append(a[-1])
        print("".join(b))
        

'''
Using While LOOP:

user_input = int(input())
for i in range(user_input):
    a = input()
    index = 1
    output = a[0]
    while index <= len(a)- 3:
        output += a[index]
        index += 2
    output += a[-1]
    print(output)

'''
