#!/usr/bin/env python
# -*- coding: utf-8 -*-

from euler import factorial
from itertools import ifilter

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def expfact(x):
    return tuple([ factorial(int(c)) for c in str(x) ])

def curious(x):
    t = expfact(x)
    return (sum(t), t)


nums = ( (x, curious(x)) for x in xrange(3, 100000) )
nums = ifilter(lambda t: t[0] == t[1][0], nums)
print sum(nums)
