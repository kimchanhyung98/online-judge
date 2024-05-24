n = int(input())

if n > 1:
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            print(divisor)
            n //= divisor
        else:
            divisor += 1
