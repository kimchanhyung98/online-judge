def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


n = int(input())
trees = [int(input()) for _ in range(n)]
distances = [trees[i] - trees[i - 1] for i in range(1, n)]

g = distances[0]
for distance in distances[1:]:
    g = gcd(g, distance)

additional_trees = 0
for distance in distances:
    additional_trees += distance // g - 1

print(additional_trees)
# print(sum(distance // g - 1 for distance in distances))
