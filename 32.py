from itertools import permutations

products = {}

for p in permutations('123456789'):
    for m in range(1, len(p) - 1):
        for n in range(m + 1, len(p)):
            a = int(''.join(p[:m]))
            b = int(''.join(p[m:n]))
            c = int(''.join(p[n:]))

            if a * b != c:
                continue

            products[c] = 1

print(sum(products.keys()))
