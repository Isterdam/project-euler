import math

# c = 1000-a-b

def find_nums():
    for i in range(1, 1000):
        for j in range(1, 1000):
            a, b, c = i, j, 1000-i-j
            if a**2 + b**2 == c**2 and a < b < c:
                return a, b, c

print(math.prod(find_nums()))
