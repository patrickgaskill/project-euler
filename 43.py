from itertools import permutations

divmap = {2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 13, 8: 17}

def tup_int(t):
    return int(''.join(t))

def subtuple(tup, i):
    return tup_int(tup[i-1 : i+2])

def has_property(p):
    return(all(subtuple(p, i) % div == 0 for (i, div) in divmap.items()))

print(sum(tup_int(p) for p in permutations('0123456789') if has_property(p)))
