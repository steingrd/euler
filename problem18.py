#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 5
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                      75
#                     95 64
#                   17 47 82
#                  18 35 87 10
#                20 04 82 47 65
#               19 01 23 75 03 34
#             88 02 77 73 07 63 67
#            99 65 04 28 06 16 70 92
#          41 41 26 56 83 40 80 70 33
#         41 48 72 33 47 32 37 16 94 29
#       53 71 44 65 25 43 91 52 97 51 14
#      70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

F = 'problem18.dat'    

def join(upper, lower):
    joined = []
    for i in range(len(lower)):
        if i == 0:
            t = (lower[i] + upper[i][0],)
        elif i == len(lower) - 1:
            t = (lower[i] + upper[i-1][0],)
        else:
            left = [ lower[i] + x for x in upper[i-1] ]
            right = [ lower[i] + x for x in upper[i] ]
            t = tuple(left+right)
        joined.append(t)
    return joined

def fold(upper, rest):
    if len(rest) > 1:
        return fold(join(upper, rest[0]), rest[1:])
    else:
        return join(upper,rest[0])

pyramide = [ [ int(x) for x in  s.split() ] for s in open(F).readlines() ]
bottomline = fold([pyramide[0]], pyramide[1:])

print max([ max(t) for t in bottomline ])

    
        


