#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at
# least two positive integers?

sums = { 
    2 : set([(1, 1)]),
}

counts = {
    2 : 1 
}

def generate_sums(n, sums):
    yield (n - 1, 1)
    for k in range(1, n):
        diff = n - k 
        if diff == 1: 
            continue
        if k > 1 and k % 2 == 1:
            yield (k, k - 1)
        for t in sums[diff]:
            yield tuple(sorted((k,) + t, reverse=True))

def count_sums(n, counts):
    c = 1
    for k in xrange(1, n):
        diff = n - k
        if diff == 1: 
            continue
        c += counts[diff]
    return c

for n in xrange(3, 6):
    sums[n] = set(generate_sums(n, sums))
    counts[n] = count_sums(n, counts)
    #print '%s, %s' % (n, len(sums[n]))

print sums[2]
print sums[3]
print sums[4]
print sums[5]

print counts[2]
print counts[3]
print counts[4]
print counts[5]



#print len(list(set(generate_sums(100, sums))))

