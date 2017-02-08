from itertools import combinations_with_replacement

def is_palindrome(n):
    s = str(n)
    return all(s[i] == s[-1-i] for i in range(len(s) // 2))

products = (a * b for a, b in combinations_with_replacement(range(100, 1000), 2))
print(max(filter(is_palindrome, products)))
