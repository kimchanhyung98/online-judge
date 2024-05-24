import sys

n, m = map(int, sys.stdin.readline().split())

baskets = list(range(1, n + 1))
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)
