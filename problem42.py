#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>
#
# The nth term of the sequence of triangle numbers is given by, 
# tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
# word value is a triangle number then we shall call the word a triangle
# word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text
# file containing nearly two-thousand common English words, how many are
# triangle words?

from euler import alphascore, OrderedGeneratorCache

F = 'words.txt'

def triangles():
    n = 1
    while True:
        n += 1
        yield (n**2 + n) / 2

cache = OrderedGeneratorCache(triangles(), initial=[1])
names = ( (s, alphascore(s)) for s in eval(open(F).read()) )
names = ( t for t in names if cache.cached(t[1]) )
print len(list(names))
