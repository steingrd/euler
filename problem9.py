#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import ifilter
from operator import add, mul

# A Pythagorean triplet is a set of three natural numbers, a<b<c, for
# which, a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c =
# 1000. Find the product abc.

def cartesian(a, b, c):
    return ( (x,y,z) for x in a for y in b for z in c )

MAX = 500

numbers = cartesian(xrange(MAX), xrange(MAX), xrange(MAX))
ordered = ifilter(lambda t: t[0]<t[1]<t[2], numbers)
thousands = ifilter(lambda t: reduce(add, t) == 1000, ordered)
triplets = ifilter(lambda t: t[0]**2 + t[1]**2 == t[2]**2 , thousands)

for t in triplets:
    print '>>>', t, reduce(mul, t)
