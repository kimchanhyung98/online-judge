def sieve_of_eratosthenes(end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(end ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    return sieve


primes = sieve_of_eratosthenes(1000000)
T = int(input().strip())
cases = [int(input().strip()) for _ in range(T)]

for n in cases:
    count = 0
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            count += 1
    print(count)
