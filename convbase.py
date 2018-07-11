#!/usr/bin/env python3
# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html
# $Id$

def convbase(n, base):
   symbols = "0123456789ABCDEF"
   if n < base:
      return symbols[n]
   else:
      return convbase(n // base, base) + symbols[n % base]

print("Converting numbers to specified bases: ")
print(convbase(1001, 3))
print(convbase(1453, 16))
print(convbase(10, 16))

print(convbase(3, 2))
print(convbase(10, 2))
print(convbase(10, 8))
