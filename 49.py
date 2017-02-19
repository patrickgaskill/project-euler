from itertools import permutations, combinations
from patrick import tup2int, is_prime

def concat_ints(ints):
    return ''.join(str(i) for i in ints)

checked = {}

# Remove the case we already know about
for p in permutations('1487'):
    checked[tup2int(p)] = True

for n in range(1000, 10000):
    if n in checked:
        continue

    perms = set([tup2int(p) for p in permutations(str(n)) if tup2int(p) > 999])

    if len(perms) < 3:
        continue

    for p in perms:
        checked[p] = True

    prime_perms = sorted([p for p in perms if is_prime(p)])

    if len(prime_perms) < 3:
        continue

    for c in combinations(prime_perms, 3):
        if c[2] - c[1] == c[1] - c[0]:
            print(concat_ints(c))
            break
    else:
        continue

    break
