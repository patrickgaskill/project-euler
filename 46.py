from patrick import is_prime

n = 3
while True:
    if not is_prime(n):
        primes = [k for k in range(2, n) if is_prime(k)]
        twice_squares = [2 * k ** 2 for k in range(1, 1 + int((n // 2) ** 0.5))]
        sums = [p + t for p in primes for t in twice_squares]
        if not n in sums:
            print(n)
            break
    n += 2
