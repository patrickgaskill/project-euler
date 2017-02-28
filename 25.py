DIGITS = 1000

a = 1
b = 1
n = 2

while b < 10 ** (DIGITS - 1):
    n += 1
    a, b = b, a + b

print(n)
