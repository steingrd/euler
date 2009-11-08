#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# The sum of the squares of the first ten natural numbers is,
# 1^ + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

UPPER = 100

sum_of_squares = sum(map(lambda x: x**2, xrange(UPPER+1)))
square_of_sums = sum(xrange(UPPER+1))**2

print square_of_sums - sum_of_squares
