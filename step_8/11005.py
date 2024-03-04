n, b = map(int, input().split())

result = ''
while n > 0:
    remainder = n % b
    if remainder < 10:
        result = str(remainder) + result
    else:
        result = chr(remainder + 55) + result
    n //= b

print(result)
