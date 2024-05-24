grid = [list(map(int, input().split())) for _ in range(9)]

value = 0
row = col = 0
for i in range(9):
    for j in range(9):
        if grid[i][j] > value:
            value = grid[i][j]
            row = i + 1
            col = j + 1

print(value)
print(max(row, 1), max(col, 1))
