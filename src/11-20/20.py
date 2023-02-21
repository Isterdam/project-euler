def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

print(sum([int(c) for c in str(fac(100))]))