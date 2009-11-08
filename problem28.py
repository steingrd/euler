#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain

# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of both diagonals is 101.
#
# What is the sum of both diagonals in a 1001 by 1001 spiral formed in
# the same way?

MAX = 1001

a = ( n**2 for n in xrange(3, MAX+1, 2) )
b = ( ((n-1)**2) - (n-2) for n in xrange(3, MAX+1, 2) )
c = ( ((n-1)**2) + 1 for n in xrange(3, MAX+1, 2) )
d = ( ((n-1)**2) + n for n in xrange(3, MAX+1, 2) )

all = chain(a, b, c, d)
print sum(all) + 1
    
