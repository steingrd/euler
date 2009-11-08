#!/usr/bin/env python
# -*- coding: utf-8 -*-

from euler import divisors
from itertools import ifilter

# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

MAX = 10000

d = lambda n: sum(divisors(n, proper=True))

def amicable(t, dnums):
    if t[1] > MAX: return False
    if t[0] == t[1]: return False
    return dnums[t[1]][1] == t[0]

dnums = [ (x, d(x)) for x in xrange(0, MAX+1) ]
anums = ( t[0] for t in dnums if amicable(t, dnums) )
print sum(anums)



