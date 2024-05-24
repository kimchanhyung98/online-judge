import sys

n, m = map(int, sys.stdin.readline().split())

baskets = [0] * n
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    for l in range(i - 1, j):
        baskets[l] = k

print(*baskets)
