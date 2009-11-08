#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import findfirst, trueforall, NumberGenerator

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
# 6x, contain the same digits.

def has_same_digits(x, y):
    x, y = str(x), str(y)
    if len(x) != len(y): 
        return False
    x, y = list(x), list(y)
    return sorted(x) == sorted(y)

def is_magic(n):
    numbers = [ n * x for x in xrange(2, 7) ]
    return trueforall(numbers, lambda x: has_same_digits(n, x))

print findfirst(NumberGenerator(start=2), is_magic)
