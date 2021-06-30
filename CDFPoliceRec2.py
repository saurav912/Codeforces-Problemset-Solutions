n = int(input())
x = list(map(int, input().split()))
crime = 0
hired = 0
for i in x:
    if i > 0:
        hired += i
    else:
        if hired == 0:
            crime += 1
        else:
            hired -= 1
print(crime)
