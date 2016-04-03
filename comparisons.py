__author__ = 'Makhtar'
# $Id: comparisons.py, c86448423bdc  makhtar $

import sys
import os
# get fibo.py
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

s1, s2, s3 = '', 'Trondheim', 'Hammer Dance'
non_null = s1 or s2 or s3
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
