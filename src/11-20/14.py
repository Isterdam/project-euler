from collections import defaultdict

def def_value():
    return 0

collatz_len = defaultdict(def_value)

def collatz(n, chain_len=0):
    # check if we have calculated for this n before
    if collatz_len[n] > 0:
        return collatz_len[n] + chain_len
    # recursion base case
    elif n == 1:
        return chain_len+1
    else:
        if n % 2 == 0:
            return collatz(n/2, chain_len+1)
        else:
            return collatz(3*n+1, chain_len+1)

# starting number and chain length
longest_chain = (0,0)

for i in range(1, 1000001):
    y = collatz(i)
    collatz_len[i] = y
    if y > longest_chain[1]:
        longest_chain = (i,y)

print(longest_chain[0])
