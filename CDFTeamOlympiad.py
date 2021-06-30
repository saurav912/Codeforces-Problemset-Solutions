user_input = int(input())
a = list(map(int, input().split()))
minimum = min(a.count(1), a.count(2), a.count(3))
index_1 = []
index_2 = []
index_3 = []
result = []
for i in range(user_input):
    if a[i] == 1:
        index_1.append(i+1)
    elif a[i] == 2:
        index_2.append(i+1)
    else:
        index_3.append(i+1)
print(minimum)
for i in range(minimum):
    print(index_1[i], index_2[i], index_3[i])
