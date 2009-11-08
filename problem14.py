#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import imap

# The following iterative sequence is defined for the set of positive
# integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one
# million.


def collect(n):
    terms = 1
    orig = n
    while n != 1:
        x = n / 2 if n & 1 == 0 else 3*n + 1
        terms += 1
        n = x
    return orig, terms

UPTO = 1*1000*1000
print max(imap(collect, xrange(2, UPTO)), key=lambda x: x[1])[0]
