import sys

c = int(sys.stdin.readline())  # unused array size
n = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(n.count(v))
