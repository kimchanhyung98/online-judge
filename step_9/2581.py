m = int(input())
n = int(input())

prime_sum = 0
min_prime = None
for num in range(m, n + 1):
    if num < 2:
        continue

    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += num
        if min_prime is None or num < min_prime:
            min_prime = num

if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(min_prime)
