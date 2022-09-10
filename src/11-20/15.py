# for a 20x20 grid, we have to take 20 total steps to the right
# and 20 total steps down to reach the bottom right.

# consider a sequence "down right down down...". The combinations
# of steps down and to the right are 40 nCr 20

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def choose(n, r):
    return fac(n) / (fac(r) * fac(n-r))

print(choose(40, 20))