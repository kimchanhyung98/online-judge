import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

m = max(scores)
for i in range(n):
    scores[i] = (scores[i] / m) * 100
# scores = [(score / m) * 100 for score in scores]
new_avg = sum(scores) / n

print(new_avg)
