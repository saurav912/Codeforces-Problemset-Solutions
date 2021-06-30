'''
x = int(input())
for i in range(x):
    a = list(map(int,input().split()))
    police = []
    crime = []
    count = 0
    for i in a:
        if i > 0:
            police.append('1')
        else:
            crime.append('1')
        if len(crime) > 0 and len(police) <= 0:
            count += 1
        elif len(crime) == 1 and len(police) >= 1:
            crime.clear()
            police.pop()
    print(count)
            
'''
n = int(input())
x = list(map(int, input().split()))
crime = 0
hired = 0
for i in x:
    if i > 0:
        hired += i
        continue
    if hired > 0 and i < 0:
        hired -= 1
        continue
    if i < 0:
        crime += 1
print(crime)
