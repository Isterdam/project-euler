a, b, c = 1, 1, 2

i = 3
while len(str(c)) < 1000:
    a, b = b, c
    c = a + b
    i += 1

print(i)