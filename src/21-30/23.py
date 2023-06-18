import math

def abundant(n):
    divs = 1
    for i in range(2, math.ceil(n/2)+1):
        if n % i == 0:
            divs += i
    return n < divs

abundants = [n for n in range(1, 28124) if abundant(n)]
pair_sums = {i+j for i in abundants for j in abundants}

res = 0
for i in range(1, 28124):
    if i not in pair_sums:
        res += i

print(res)