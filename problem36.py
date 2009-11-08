#!/usr/bin/env python
# -*- coding: utf-8 -*-

from euler import palindrome

# The decimal number, 585 = 10010010012 (binary), is palindromic in
# both bases.
#
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not
# include leading zeros.)

MAX = 1000*1000

bstr = lambda n: n>0 and bstr(n>>1)+str(n&1) or ''

p = ( x for x in xrange(1, MAX) if palindrome(x) and palindrome(bstr(x)) )
print sum(p)
