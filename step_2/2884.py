h, m = map(int, input().split())

m -= 45
if m < 0:
    m += 60
    # h = (h - 1) % 24
    h -= 1
    if h < 0:
        h = 23

print(h, m)
