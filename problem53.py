#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import factorial
from itertools import count, ifilter, izip

# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of nCr, for 1 <= n <= 100,
# r <= n, are greater than one-million?

def ncr(n, r):
    nfac, rfac, nrfac = factorial(n), factorial(r), factorial(n - r)
    return nfac / (rfac * nrfac)

def for_all_r(n):
    for r in xrange(0, n + 1):
        yield ncr(n, r)
    
results = ( result for n in xrange(1, 101) for result in for_all_r(n) )
million = ifilter(lambda t: t > 1000000, results)
counted = zip(count(1), million)

print len(counted)
    
