#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

F = 'triangle.txt'

def join(up, lo):
    print up
    print lo
    print ','
    return [ up[i] + max(lo[i],lo[i+1]) for i in xrange(len(up)) ]

def fold(lo, rest):
    if len(rest) == 1:
        return join(rest[0], lo)
    else:
        return fold(join(rest[-1], lo), rest[:-1])

pyramide = [ [ int(x) for x in  s.split() ] for s in open(F).readlines() ]

print fold(pyramide[-1], pyramide[:-1])
        
