__author__ = 'makhtar'

# $Id: format.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
# Input formatting

import math

# printf style
print('The value of PI is approximately %5.3f' % math.pi)

# table of squares and cubes, right justified
for x in range(1, 11):
    print(repr(x).rjust(2).zfill(2), repr(x * x).rjust(3), end=' ')
    # Note the use of 'end' on previous line
    print(repr(x * x * x).rjust(4))

# Different method
for x in range(1, 11):
    print('{0:+>2d} {1:>3d} {2:>4d}'.format(x, x * x, - x * x * x))

# zero padding
print('\n', '12'.zfill(5))
print('We are the {} who say "{}!\n"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))

# use '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) to apply formatting
#pi = str(math.pi)[0:4]
print('The value of PI is approximately {!r}.'.format(math.pi))

# as in C, specify the number of decimals
print('The value of PI is approximately {:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 76789}
for name, phone in table.items():
    print('{0:10} ==> {1:<8d}'.format(name, phone))

# Base convertions
print("\nBinary of {:d} is {:b}".format(8, 8))

print("\nint: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# Templates
from string import Template
s = Template('$who likes $what')
print("\n", s.substitute(who='tim', what='kung pao') )
