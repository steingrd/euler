#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from euler import findfirst, permutations, NumberGenerator, OrderedGeneratorCache

# The cube, 41063625 (345^3), can be permuted to produce two other
# cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the
# smallest cube which has exactly three permutations of its digits which
# are also cube.
#
# Find the smallest cube for which exactly five permutations of its
# digits are cube.

def int_permutations(x):
    return map(int, map(''.join, permutations(str(x))))

def count_cube_permutations(x):
    count = 0
    checked = set()
    for p in int_permutations(x):
        if p in checked: 
            continue
        checked.add(p)
        if cube_cache.cached(p):
            count += 1
    return count


cube_cache = OrderedGeneratorCache( x ** 3 for x in NumberGenerator(start=2) )
cube_generator = ( x ** 3 for x in NumberGenerator(start=2) )
cube_counter = ( (x, count_cube_permutations(x)) for x in cube_generator )

print findfirst(cube_counter, lambda t: t[1] == 5)
