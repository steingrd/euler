#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from itertools import imap

# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

def to_english(num):
    if num == 1000:
        return 'one thousand'

    basics  = { 
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
        11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }
    tens    = { 
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety' }
    
    start = str(num)[-2:]
    rest = str(num)[:-2]

    s = int(start[-2:])
    if s != 0 and s < 20:
        english = basics[s]
    elif s != 0:
        if s % 10 == 0:
            english = tens[s/10]
        else:
            english = '%s-%s' % (tens[s/10], basics[s%10])
    else:
        english = ''

    if rest:
        s = int(rest[-1])
        if english:
            english = basics[s] + ' hundred and ' + english
        else:
            english = basics[s] + ' hundred'

    return english


def count(s):
    s = s.replace(' ', '')
    s = s.replace('-', '')
    return len(s)

print sum(imap(count, imap(to_english, xrange(1, 1001))))
