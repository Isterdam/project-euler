x = 2 ** 1000
a = 0

while x > 0:
    a += x % 10
    x //= 10 # floor division

print(a)