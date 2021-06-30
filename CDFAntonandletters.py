a = list(input()[1:-1].split(','))
for i in range(len(a)):
    if a[i] == '':
        a = []
    else:
        a[i] = a[i].strip()
print(len(set(a)))
