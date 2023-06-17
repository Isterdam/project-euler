names = open("names.txt", "r").read().replace("\"", "").split(",")
names = sorted(names)

def score(name):
    return sum(ord(c)-64 for c in name)

res = 0
for i in range(len(names)):
    res += score(names[i])*(i+1)

print(res)