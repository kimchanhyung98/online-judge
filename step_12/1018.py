n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_repaint = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        repaint_count = 0
        for row in range(i, i + 8):
            for col in range(j, j + 8):
                if (row + col) % 2 == 0 and board[row][col] != 'W':
                    repaint_count += 1
                elif (row + col) % 2 == 1 and board[row][col] != 'B':
                    repaint_count += 1

        min_repaint = min(min_repaint, repaint_count, 64 - repaint_count)

print(min_repaint)
