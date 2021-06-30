x = int(input())
a = input()
count = 0
a= list(a)
for j in range(1,x):
    if a[j] == a[j-1]:
        count = count + 1
print(count)
