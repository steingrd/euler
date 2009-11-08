#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>


# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#
# [ ... problem13.dat ]

F = 'problem13.dat'

nums = [ long(c) for c in open(F).readlines() ]
print str(sum(nums))[:10]
