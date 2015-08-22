__author__ = 'Makhtar'
"""
Demo formatting I/O
$Id$
"""

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

b = int(input("Please enter another integer: "))

print("Floor division test ", x, "//", b, ": " + str(x // b))

print(str(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))
