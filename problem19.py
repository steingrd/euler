#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You are given the following information, but you may prefer to do
# some research for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#  * A leap year occurs on any year evenly divisible by 4, but not
#   on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta
from itertools import ifilter, izip, count

def days(start=date(1901, 01, 01), end=date(2000, 12, 31)):
    d = start
    while d <= end:
        yield d
        d = d + timedelta(1)

print len(list(ifilter(lambda d: d.day == 1 and d.isoweekday() == 7, days())))
