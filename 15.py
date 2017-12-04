#!/usr/bin/env python3
import re

theInput = """Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has 5 positions; at time=0, it is at position 0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has 3 positions; at time=0, it is at position 0.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 19 positions; at time=0, it is at position 17."""

discMatcher = re.compile("Disc #(\d) has (\d+) positions;" +
                         " at time=(\d), it is at position (\d+).")


def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)



theInput = theInput.split('\n')

theDiscs = []
for line in theInput:
    results = discMatcher.match(line)
    theDiscs.append(list(int(i) for i in results.groups())[1:4:2])


# we shift each disk, so that way we only need to find when they are all at 0
for i in range(len(theDiscs)):
    theDiscs[i][1] += i+1
    theDiscs[i][1] %= theDiscs[i][0]

# the algorithm:
# align the first disc
# align another disc, by jumping using the lcm, till finished


print(theDiscs)
