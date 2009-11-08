#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import ifilter

# An irrational decimal fraction is created by concatenating the
# positive integers:
#
# 0.123456789101112131415161718192021...
#              ^
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value
# of the following expression.
#
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

def digit_generator(up_to=None):
    i = 1
    while i < up_to:
        s = str(i)
        i += 1
        for c in s: 
            yield c

MAX_INT = 185186

parts = (1, 10, 100, 1000, 10000, 100000, 1000000)
numbers = digit_generator(MAX_INT)
numbers = ifilter(lambda t: t[0]+1 in parts, enumerate(numbers))
numbers = ( int(t[1]) for t in numbers )

print reduce(lambda x, y: x * y, numbers, 1)
