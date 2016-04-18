#!/usr/bin/env python3
"""
Detect prime numbers
Makhtar Diouf
$Id$
"""
from makhtar import utils as ut

l = range(50)
print([(_, ut.isprime(_)) for _ in l if ut.isprime(_)])
