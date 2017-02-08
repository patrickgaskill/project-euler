from patrick import factors

def triangle_number(n):
    return (n * (n + 1)) // 2

NUM_DIVISORS = 500

i = 1
while True:
    t = triangle_number(i)
    if (len(factors(t)) > NUM_DIVISORS):
        print(t)
        break
    i += 1
