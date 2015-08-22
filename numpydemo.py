__author__ = 'Makhtar'

"""
Demoing features provided by the popular numpy package
Download a full scipy distro from http://continuum.io/downloads#py34
might have to past this to the ipython from the Anaconda prompt first
"""
import os

import numpy as np


def calc(set):
    for i in set:
        i = pow(i, 2)
    return i


L = range(1000)

# timeit.timeit('calc(L)')
print(os.times())

a = np.arange(1000)
print(a)
# inverse
print(a[::-1])

# print(a**2)

a = np.array([0, 1, 2, 3])
print(a.ndim)
print(a.shape)
# triangles
np.tril(a)
np.triu(a)

# linear space

c = np.linspace(0, 1, 6)  # start, end, num-points
np.ones((3, 3))
np.eye(3)  # identity matrix
np.eye(4) == np.identity(4)

np.diag(np.array([1, 2, 3, 4]))  # diagonal array

# Fancy indexing
np.random.seed(3)
a = np.random.random_integers(0, 10, 5)
print(a)
# array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
(a % 3 == 0)

mask = (a % 3 == 0)
extract_from_a = a[mask]  # or,  a[a%3==0]
extract_from_a  # extract a sub-array with the mask

a = np.arange(0, 100, 10)
print(a)
print(a[[2, 3, 2, 4, 2]])

# masked arrays
x = np.ma.array([1, 2, 3, 4], mask=[0, 1, 0, 1])
print(x)

y = np.ma.array([1, 2, 3, 4], mask=[0, 1, 1, 1])
print(x + y)

