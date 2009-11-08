#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import factorial

# n! means n * (n - 1) * ... * 3 * 2 * 1
#
# Find the sum of the digits in the number 100!

print sum(map(int, str(factorial(100))))
