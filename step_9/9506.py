while True:
    n = int(input())

    if n == -1:
        break

    factors = [1]
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)

    if sum(factors) == n:
        factor_str = ' + '.join(map(str, factors))
        print(f"{n} = {factor_str}")
    else:
        print(f"{n} is NOT perfect.")
