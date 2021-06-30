x = int(input())
y = list(map(int,input().split()))
small = [y[0]]
large = [y[0]]
for i in range(len(y)):
    if y[i] > max(large):
        large.append(y[i])
    if y[i] < min(small):
        small.append(y[i])
ans = (len(small)-1)+(len(large)-1)
print(ans)
