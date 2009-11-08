#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import palindrome

# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def cartesian(a, b):
    return tuple([ (x,y) for x in a for y in b ])

pairs = cartesian(xrange(100,1000), xrange(100, 1000))
palindromes = filter(palindrome, [ x[0]*x[1] for x in pairs ])
print max(palindromes)
