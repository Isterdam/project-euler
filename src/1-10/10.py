def eratosthenes(n):
    primes = []
    xs = set(i for i in range(2, n+1))

    while len(xs) > 0:
        p = xs.pop()
        primes.append(p)
        for i in range(p*2, n+1, p):
            if i in xs:
                xs.remove(i)

    return primes

print(sum(eratosthenes(2 * 10**6)))