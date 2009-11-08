#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import findfirst, trueforall

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest number that is evenly divisible by all of the
# numbers from 1 to 20?

MAX = 1000*1000*1000

def is_magic(x, numbers):
    return trueforall(numbers, lambda e: x % e == 0)

print findfirst(xrange(20, MAX, 20), lambda x: is_magic(x, range(1, 21)))

