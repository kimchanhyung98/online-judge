n, m = map(int, input().split())

a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

b = []
for _ in range(n):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(n):
    result_row = []
    for j in range(m):
        result_row.append(a[i][j] + b[i][j])

    print(*result_row)
