__author__ = 'Makhtar'
"""
Demo trivial I/O formatting
"""
import sys
from makhtar import utils as ut

x = int(input("Please enter an integer: "))

if x < 0:
    print("Negative number detected")
elif x == 0:
    print('Null number detected')
else:
    print('Positive number detected')

b = int(input("Please enter another integer: "))

print(f"Floor division test {x} // {b}: {str(x // b)}")

print(1 / 7)

x = 10 * 3.25
y = 20 * 20
s = f'The value of x is {x}, and y is {y}...'
print(s)

ut.logit("Done running {}".format(sys.argv[0]))
