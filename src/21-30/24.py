from itertools import permutations

l = sorted(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
print("".join(l[999_999]))
