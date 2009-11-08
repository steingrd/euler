#!/usr/bin/env python

# Copyright (c) 2008 by Steingrim Dovland <steingrd@ifi.uio.no>

from operator import mul

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphascore(s):
    """
    Returns the 'score' of the given string. Each letter in s is given a
    score by its alphabetical position, the score of s is the sum of the
    scores of its letters.

    >>> alphascore('abc')
    6
    >>> alphascore('ABC')
    6
    >>> alphascore('aBc')
    6
    >>> alphascore('__A')
    1
    >>> alphascore('')
    0

    """
    return sum([ alphabet.find(c.upper())+1 for c in s 
                 if c.upper() in alphabet ])

def combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in combinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def permutations(items):
    return combinations(items, len(items))

def factorial(n):
    """
    Returns the factorial of n, n!, i.e. 1*2*3*...*n

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6

    """
    return reduce(mul, xrange(1, n+1), 1)

def palindrome(num):
    """
    Returns true if `num' is a palindromic number.

    >>> palindrome(121)
    True
    >>> palindrome(12321)
    True
    >>> palindrome(12322)
    False
    
    """
    num = str(num)
    return num == num[::-1]

def fib(max=None):
    """
    Returns a generator for Fibonacci numbers. The generator starts
    out with 1 1 2 and continues forever or until it reaches `max'
    inclusive.

    >>> ' '.join([ str(x) for x in fib(3) ])
    '1 1 2 3'
    >>> ' '.join([ str(x) for x in fib(10) ])
    '1 1 2 3 5 8'
    >>> ' '.join([ str(x) for x in fib(1) ])
    '1 1'
    
    """
    i = 1
    j = 0
    while not max or i <= max:
        yield i
        x = j
        j = i
        i = i + x

def findfirst(iterable, predicate):
    """
    Locates the first element in `iterable' that returns true when
    `predicate' is invoked with the element as its only argument.

    Returns None if the list is empty or if no element in the list
    satisfies the predicate. 
    
    >>> findfirst([1,2,3,4,5], lambda x: x > 3)
    4
    >>> print findfirst([], lambda x: x > 3)
    None
    >>> print findfirst([1,2,3,4,5], lambda x: x > 5)
    None
    
    """
    for elm in iterable:
        if predicate(elm): return elm

def trueforall(iterable, predicate):
    """
    Returns True if `predicate' evalutes to true when invoked on each
    element of iterable, False otherwise.

    >>> trueforall([2,4,6,8], lambda x: x%2 == 0)
    True
    >>> trueforall([2,4,6,8,9], lambda x: x%2 == 0)
    False
    
    """
    for elm in iterable:
        if not predicate(elm): return False
    return True

def slide(slicable, size):
    """
    Returns a generator that is a sliding window over `slicable'. The
    size of the window is `size' elements wide.

    >>> [ x for x in slide('abcdef', 2) ]
    ['ab', 'bc', 'cd', 'de', 'ef']
    >>> [ x for x in slide('abcdef', 3) ]
    ['abc', 'bcd', 'cde', 'def']
    >>> [ x for x in slide('abc', 1) ]
    ['a', 'b', 'c']
    
    """
    i = 0
    while i + size < len(slicable):
        yield slicable[i:i+size]
        i += 1
    yield slicable[-size:]

def divisors(x, proper=True):
    """
    Returns a tuple of factors for the given number x. The list
    includes 1 and if proper is False it also includes x.

    >>> divisors(220)
    (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
    >>> divisors(220, proper=False)
    (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220)
    >>> divisors(1)
    ()
    >>> divisors(1, proper=False)
    (1,)
    >>> divisors(0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer division or modulo by zero
    
    """
    if x == 0:
        raise ZeroDivisionError, "integer division or modulo by zero"
    result  = [ 1 ] if x != 1 else []
    result += [ i for i in xrange(2, x) if x % i == 0 ]
    if not proper:
        result.append(x)
    return tuple(result)

def primefactors(x):
    """
    Returns a tuple of prime factors for the given number x.
    
    """
    check = 2
    newnum = x
    numbers = []
    while check*check <= newnum:
        if newnum % check == 0:
            numbers.append(check)
            newnum = newnum / check
        else:
            check += 1
    if newnum != 1:
        numbers.append(newnum)
    return tuple(numbers)

def primes(n):
    """ 
    Returns a tuple of prime numbers from 2 to n inclusive.

    >>> primes(10)
    (2, 3, 5, 7)
    >>> primes(0)
    ()
    >>> primes(-1)
    ()
    >>> primes(2)
    (2,)

    """
    if n < 2:  return ()
    if n == 2: return (2,)
    # only odd numbers starting at 3
    s = range(3, n, 2)
    # n**0.5 may be slightly faster than math.sqrt(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    # make exception for 2
    return tuple([2]+[x for x in s if x])

class DefaultDict(dict):
    def __init__(self, default):
        dict.__init__(self)
        self.default = default
    
    def __setitem__(self, key, val):
        if not self.has_key(key):
            dict.__setitem__(self, key, self.default)
        dict.__setitem__(self, key, val)

    def __getitem__(self, key):
        if not self.has_key(key):
            return self.default
        return dict.__getitem__(self, key)

class OrderedGeneratorCache(object):
    def __init__(self, generator, initial=None):
        self.generator = generator
        self.cache = [ self.generator.next() ]
        if initial:
            self.cache += list(initial)

    def cached(self, x):
        # increase the cache as much as needed
        while self.cache[-1] <= x:
            self.cache.append(self.generator.next())
        return x in self.cache
        
class NumberGenerator(object):
    def __init__(self, start=0, max=None):
        self.n = start
        self.max = max

    def __iter__(self):
        if self.max:
            while self.n < self.max:
                yield self.n
                self.n += 1
        else:
            while True:
                yield self.n
                self.n += 1

class PrimeGenerator(object):
    def __init__(self, max=None):
        self.i = -1
        self.n = 2
        self.primes = [ 2 ]
        self.max = max if max else -1

    def next(self):
        if self.n >= self.max and self.max != -1:
            raise StopIteration

        if self.i >= len(self.primes) - 1:
            self.n *= 2
            self.primes = primes(self.n)
        self.i += 1
        return self.primes[self.i]

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = [] if not next else next

    def __repr__(self):
        return 'Node(%s, next=%s)' % (repr(self.value), repr(self.next))

    def addnext(self, n):
        assert isinstance(n, node)
        self.next.append(n)


def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()
