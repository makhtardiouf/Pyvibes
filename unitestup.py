__author__ = 'Makhtar'

def average(values):
    """Computes the arithmetic mean of a list of numbers.

     print(average([20, 30, 70]))
    40.0
    """
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        print("Error: division by zero ", values)
        return 0


import doctest
# or use unittest for more detailed tests

print(doctest.testmod())   # automatically validate the embedded tests

val = range(10)
print(average(val))
