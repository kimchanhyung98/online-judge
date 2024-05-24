a, b, c = map(int, input().split())

max_length = max(a, b, c)
rest_length = sum([a, b, c]) - max_length
if max_length < rest_length:
    print(sum([a, b, c]))
else:
    print(rest_length * 2 - 1)
