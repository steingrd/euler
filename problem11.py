#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from operator import mul
from euler import slide

# In the 20x20 grid below, four numbers along a diagonal line have been
# marked in red.
#
# [ ... see problem11.dat ]
# 
# The product of these numbers is 26 * 63 * 78 * 14 = 1788696.
#
# What is the greatest product of four numbers in any direction (up,
# down, left, right, or diagonally) in the 20x20 grid?

F = 'problem11.dat' # data file
C = 4               # number of consecutive integers

def horisontal():
    f = lambda l: [ int(x) for x in l ]
    return [ f(l.strip().split()) for l in open(F).readlines() if l.strip() ]

def vertical():
    hlines = horisontal()
    return [ [ line[i] for line in hlines ] for i in xrange(len(hlines)) ]

def diagonal(direction):
    hlines = horisontal()
    offset = len(hlines)
    dlines = [ [] for i in xrange(offset * 2 + 1) ]
    for i in xrange(len(hlines)):
        for j in xrange(len(hlines[i])):
            dlines[direction(i,j,offset)].append(hlines[i][j])
    return filter(lambda x: len(x) >= C, dlines)

# functions for traversing diagonally
up = lambda i, j, o: i + j
down = lambda i, j, o: i - j + o

lines = horisontal() + vertical() + diagonal(up) + diagonal(down)
numbers = [ n for x in lines for n in slide(x, C) ]
products = [ reduce(mul, nums) for nums in numbers ]
print max(products)
