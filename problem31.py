#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# In England the currency is made up of pound, £, and pence, p, and
# there are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
#     1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can £2 be made using any number of coins?

import sys
from itertools import ifilter
        
max_of_coin = [ 200, 100, 40, 20, 10, 4, 2 ]
circulation = (1, 2, 5, 10, 20, 50, 100)
number_of_coins = len(circulation)

def sum_of_coins(coins):
    return sum([ x*y for x,y in zip(circulation, coins) ])

def generate_combinations(index, coins):
    sum = sum_of_coins(coins)
    if sum > 200:
        yield
    if index == number_of_coins:
        if sum == 200:
            yield coins
    else:
        for spin in xrange(max_of_coin[index] + 1):
            coins[index] = spin
            for c in generate_combinations(index + 1, coins):
                if c: yield c
    
coins = generate_combinations(0, [0] * number_of_coins)

count = 0
for c in coins:
    count += 1
    if count % 10 == 0: 
        sys.stdout.write('.')
        sys.stdout.flush()
print count
