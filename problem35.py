#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
#
#  197 
#  719
#  971
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31,
# 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from euler import OrderedGeneratorCache, PrimeGenerator

def rotate(s):
    s = str(s)
    for i, c in enumerate(s):
        yield int(s[i:] + s[:i])

def circular(p, primes):
    for pr in rotate(p):
        if not primes.has_key(pr): return False
    return True

def find_circular(primes):
    return [ p for p in primes.iterkeys() if circular(p, primes) ]

def contains_even(p):
    for c in str(p):
        if c in '2468': return True
    return False

def create_cache(max):
    primegen = PrimeGenerator()
    primecache = dict()
    p = primegen.next()
    while p < max:
        if not contains_even(p):
            primecache[p] = p
        p = primegen.next()
    return primecache
        
if __name__ == '__main__':
    primes = create_cache(1000*1000)
    print(len(find_circular(primes)))
    
