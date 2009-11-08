#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import count, imap, izip
from euler import alphascore

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text
# file containing over five-thousand first names, begin by sorting it
# into alphabetical order. Then working out the alphabetical value for
# each name, multiply this value by its alphabetical position in the
# list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?

F = 'names.txt'

names = sorted(eval(open(F).read()))
names = imap(lambda n: (alphascore(n), n), names)
names = izip(count(1), names)
score = imap(lambda x: x[0] * x[1][0], names)
print sum(score)

