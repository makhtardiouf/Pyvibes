__author__ = 'makhtar'

# $Id$
# another standard sequence data type: the tuple; is however immutable

t = 12345, 54321, 'hello!'
print(type(t), "t[0]=", t[0])

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print("\n", u)
