n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((y, x))

sorted_points = sorted(points)
for point in sorted_points:
    print(point[1], point[0])
