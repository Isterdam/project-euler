import math

def triangular(x):
    return x*(x+1)/2

def divisors(x):
    divisors = 0
    limit = math.ceil(math.sqrt(x))

    for i in range(1, limit+1):
        if x % i == 0:
            divisors += 1
            if i != x/i:
                # x/i is also a divisor
                divisors += 1
    
    return divisors

i = 1
while True:
    t = int(triangular(i))
    if divisors(t) > 500:
        print(t)
        break
    i += 1