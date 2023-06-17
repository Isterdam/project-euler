import math

def d(n):
    divs = 0
    for i in range(1, math.ceil(n/2)+1):
        if n % i == 0:
            divs += i
    return divs

res = 0
for a in range(10_000):
    b = d(a)
    if a != b and d(b) == a:
        res += a

print(res)
