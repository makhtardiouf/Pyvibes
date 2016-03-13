__author__ = 'makhtar'

# $Id: tuples.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
__doc__
'''another standard sequence data type: the tuple; is immutable
  Consists of a number of values separated by commas.
  Usually contain an heterogeneous sequence of elements that are accessed via unpacking or indexing
'''

t = 12345, 54321, 'hello!'
print(type(t), "t[0]=", t[0])

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print("\n", u)

# unpacking
x, y = u
print(x)