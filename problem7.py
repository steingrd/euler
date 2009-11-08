#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import primes

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
#
# What is the 10001st prime number?

print primes(1000*1000)[10000]
