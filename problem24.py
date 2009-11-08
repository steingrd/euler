#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import count, izip
from euler import permutations, findfirst

# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?

p = permutations('0123456789')
x = findfirst(izip(count(1), p), lambda x: x[0] == 1*1000*1000)
print ''.join(x[1])

