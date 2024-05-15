n, m = map(int, input().split())
s = set(input().strip() for _ in range(n))

count = 0
for _ in range(m):
    word = input().strip()
    if word in s:
        count += 1

print(count)
