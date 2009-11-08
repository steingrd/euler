#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# Starting in the top left corner of a 2×2 grid, there are 6 routes
# (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20×20 grid?

from itertools import ifilter
from euler import combinations

N = 20
V = N+1
X = 0

def steps(v):
    if v % V != V-1: yield v + 1
    if v < V**2 - V: yield v + V

def paths(v):
    if v == (V**2) - 1:
        global X
        X += 1
    
    if v % V != V-1: paths(v+1)
    if v < V**2 - V: paths(v+V)

    #return [ [v] + pn for vn in steps(v) for pn in paths(vn) ]


from pprint import pprint
x = paths(0)
print X





