n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_points = sorted(points)
for point in sorted_points:
    print(point[0], point[1])
