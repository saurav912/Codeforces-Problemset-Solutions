x = list(map(int,input().split()))
a = x[1]*x[2]
toasts = a //x[6]
limes = x[3]*x[4]
salts = x[5] // x[7]
print((min(toasts,limes,salts)//x[0]))
