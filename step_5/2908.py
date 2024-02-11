a, b = input().split()
reverse_a = int(a[::-1])
reverse_b = int(b[::-1])

print(reverse_a if reverse_a > reverse_b else reverse_b)
