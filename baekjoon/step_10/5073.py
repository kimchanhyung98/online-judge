while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    max_side = max(a, b, c)
    if max_side >= a + b + c - max_side:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
