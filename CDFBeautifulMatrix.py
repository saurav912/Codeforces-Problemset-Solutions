i = col = row = 0
matrix = list()
for _ in range(5):
    matrix.append(input().split())
while i < 5:
    j = 0
    while j < 5:
        if matrix[i][j] == '1':
            row = i
            col = j
            break
        j += 1
    i += 1
print(abs(row-2) + abs(col-2))
