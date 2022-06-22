def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = [x * y 
    for x in range(100, 1000)
    for y in range(100, 1000)
    if is_palindrome(x * y)]

print(max(palindromes))

