def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


a, b = map(int, input().split())
c, d = map(int, input().split())
numerator = a * d + b * c  # 분자
denominator = b * d  # 분모
g = gcd(numerator, denominator)

print(numerator // g, denominator // g)
