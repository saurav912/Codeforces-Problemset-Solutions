user_input = int(input())
max_passenger = []
for i in range(user_input):
    a,b = list(map(int,input().split()))
    if len(max_passenger) == 0:
        max_passenger.append(b-a)
    else:
        max_passenger.append((max_passenger[-1] - a) + b)
print(max(max_passenger))
