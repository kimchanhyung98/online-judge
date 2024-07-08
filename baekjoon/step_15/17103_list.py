def sieve_of_eratosthenes(end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(end ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    return sieve


def count_goldbach_partitions(n, is_prime):
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1

    return count


primes = sieve_of_eratosthenes(1000000)
T = int(input().strip())
cases = [int(input().strip()) for _ in range(T)]

results = [count_goldbach_partitions(n, primes) for n in cases]
for result in results:
    print(result)
