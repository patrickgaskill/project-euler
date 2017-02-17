from itertools import permutations
from patrick import tup2int

divmap = {2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 13, 8: 17}

def subtuple(tup, i):
    return tup2int(tup[i-1 : i+2])

def has_property(p):
    return(all(subtuple(p, i) % div == 0 for (i, div) in divmap.items()))

print(sum(tup2int(p) for p in permutations('0123456789') if has_property(p)))
