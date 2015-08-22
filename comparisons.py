__author__ = 'Makhtar'
# $Id$

import sys
import os

import fibo

# from makhtar import utils

# utils.showMsg(sys.platform, sys.version)
print("Running on platform: ", sys.platform, sys.version, os.name)
# showMsg = utils.showMsg
if "linux" in sys.platform:
    pass
    # utils.showMsg(os.uname())

print("System path:")
for p in sys.path:
    print(p)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

a = 4
b = 5
c = 5
print(a < b == c)
print(a and (not b) and c)

print((1, 2, 3) < (1, 2, 4))
print([1, 4, 3] < [1, 2, 4])

print('Pascal' < 'Python')

fibo.fib(10)
x = fibo.fib2(10)
y = fibo.fib2(20)
print(x, y)
print(fibo.__name__)

# Show defined vars and modules members
# print(dir())
