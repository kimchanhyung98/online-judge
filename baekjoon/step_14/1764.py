n, m = map(int, input().split())
heard, seen = set(), set()

for _ in range(n):
    name = input().strip()
    heard.add(name)

for _ in range(m):
    name = input().strip()
    seen.add(name)

heard_and_seen = heard.intersection(seen)
print(len(heard_and_seen))
for name in sorted(heard_and_seen):
    print(name)
