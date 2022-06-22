def prime_factors(n):
    prime_factors = []

    i = 2
    while n > 1:
        while n % i == 0:
            prime_factors.append(i)
            n /= i
        i += 1

    return prime_factors

print(max(prime_factors(600851475143)))