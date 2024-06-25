def sieve_of_eratosthenes(start, end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(end ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    for num in range(start, end + 1):
        if sieve[num]:
            print(num)


m, n = map(int, input().split())
sieve_of_eratosthenes(m, n)
