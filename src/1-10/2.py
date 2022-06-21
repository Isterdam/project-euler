prev, next = 1, 2
ans = 0

while next < 4 * (10**6):
    if next % 2 == 0:
        ans += next
    prev, next = next, prev + next

print(ans)

