def sieve_of_eratosthenes(end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(end ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    return sieve


primes = sieve_of_eratosthenes(123456 * 2)
while True:
    n = int(input().strip())
    if n == 0:
        break

    print(sum(1 for i in range(n + 1, n * 2 + 1) if primes[i]))
