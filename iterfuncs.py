#!/usr/bin/env python3
"""
Itertools module: functions creating iterators for efficient looping
Makhtar Diouf
$Id$
"""
from itertools import *
import operator

a = count(10)
print("Count: ", a)

# This repeats indefinitely
print("Cycle: ", cycle('ABCD').__next__())
print("Repeat:", repeat(10, 5).__next__())

print("Accum:", accumulate(range(10)))
print("Accum with func:", accumulate(range(10), max))

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(accumulate(data, operator.mul)))
print(list(accumulate(data, max)))
b = chain(data, a)
print(b)

c = dropwhile(lambda x: x < 9, data)
print(list(c))

print(list(permutations("abc")))
