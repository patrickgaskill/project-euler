def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

cache = {1: 1}

def steps(n):
    if n in cache:
        return cache[n]

    s = 1 + steps(collatz(n))
    cache[n] = s
    return s

for i in range(1, 1000000):
    steps(i)

print(max(cache, key=lambda k: cache[k]))
