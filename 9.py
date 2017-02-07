SUM = 1000

for a in range(1, SUM + 1):
    for b in range(a, SUM - a):
        c = SUM - a - b
        if a*a + b*b == c*c:
            print(a * b * c)
            break
    else:
        continue
    break
