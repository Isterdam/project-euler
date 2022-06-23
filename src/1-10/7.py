import math

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

# ~n/log(n) primes smaller than n
n = 100
while n / math.log(n) < 10001:
    n += 100

print(eratosthenes(n)[10000])
