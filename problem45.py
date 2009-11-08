#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# Triangle, pentagonal, and hexagonal numbers are generated by the
# following formulae:
#
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...
#
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

MAXN = 100000

tri = lambda n: (n*(n+1))/2
pent = lambda n: (n*((3*n)-1))/2
hex = lambda n: n*((2*n)-1)

tricache = dict()
hexcache = dict()
pentcache = dict()

for n in xrange(2, MAXN):
    t = (n, tri(n))
    tricache[t[1]] = t

    p = (n, pent(n))
    pentcache[p[1]] = p

    h = (n, hex(n))
    hexcache[h[1]] = h

nums = [ t for t in tricache.iterkeys() 
         if pentcache.has_key(t) and hexcache.has_key(t) ]

tups = [ (tricache[t],hexcache[t],pentcache[t]) for t in nums ]
print tups
print nums[-1]
