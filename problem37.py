#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from itertools import chain, imap
from euler import trueforall as all, PrimeGenerator

MAX = 10000

def getprimes(n):
    cache = {}
    primes = []
    gen = PrimeGenerator()
    for i in xrange(n):
        p = gen.next()
        primes.append(p)
        cache[p] = p
    return primes, cache

primes, cache = getprimes(59600)
prime = lambda x: cache.has_key(x)
left  = lambda s: [ s[i:] for i in xrange(len(s)) ]
right = lambda s: [ s[:i] for i in reversed(xrange(len(s)+1)) if s[:i] ]
trunc = lambda x: all(imap(int, chain(left(str(x)), right(str(x)))), prime)
t = [ p for p in primes if trunc(p) ]
t = filter(lambda t: t > 10, t)
print t
print sum(t)

