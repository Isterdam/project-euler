denoms = range(20, 1, -1)

def divisble_by_all(n):
    for d in denoms:
        if n % d > 0:
            return False
    return True

i = 20
while True:
    if divisble_by_all(i):
        print(i)
        break
    i += 20