#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# A googol (10^100) is a massive number: one followed by one-hundred
# zeros; 100^100 is almost unimaginably large: one followed by
# two-hundred zeros. Despite their size, the sum of the digits in each
# number is only 1.
#
# Considering natural numbers of the form, a^b, where a, b < 100, what
# is the maximum digital sum?

LOW = 90
LIM = 100

d = lambda x: sum([ int(c) for c in str(x) ])

digsums = ( (a,b,d(a**b)) for a in xrange(LOW, LIM) for b in xrange(LOW, LIM) )
print max(digsums, key=lambda t: t[2])[2]
