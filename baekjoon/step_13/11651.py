n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((y, x))

for point in sorted(points):
    print(point[1], point[0])
