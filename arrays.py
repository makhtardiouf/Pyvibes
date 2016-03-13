__author__ = 'makhtar'
# Trivial arrays operations
# $Id: arrays.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
import sys
import time
from makhtar import utils as ut

a = ['Mary', 'had', 'a', 'little', 'lamb']
a.sort()
for i in range(len(a)):
    print(i, a[i])

b = []
# range with step
for i in range(0, len(a), 2):
    b.append(a[i] + " starts with " + a[i][0])

print(b)

for i in range(len(a[0])):
    # print letters backwards
    sys.stdout.write(a[i][len(a[i]) - i - 1])
    sys.stdout.flush()
    time.sleep(0.2)

# Multidimentional arrays
rows = [[1] * 5 for i in range(5)]
print(rows)
# empty on
# r = [[]]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters)

# See how to iterate from 'a' to 'g', as in C
# r = range(g)
# for i in r:
#     letters.append(i)

# Clear
letters[:] = []
letters

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1], x[1][1])

vec = [-4, -2, 0, 2, 4]
vec = [x * 2 for x in vec]
# filter the list to exclude negative numbers
v2 = [x for x in vec if x >= 0]
print(v2)

# apply a function to all the elements
v2 = [abs(x) for x in vec]
print(v2)

# Transpose matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
v = [[row[i] for row in matrix] for i in range(4)]

# simpler way
v2 = list(zip(*matrix))
print(v2[0][1])
print("Transposing matrix: \n", matrix, "\n", v, "\n", v2)

# delete elem, row or entire vector
# del(v[0])
del v


rows = matrix
print(len(rows), len(rows[0]))

for i in range(len(rows)):
    total = 0;
    sumCol = 0
    for j in range(len(rows[i])):
        #total += rows[i][j]
        sumCol += rows[j-1][i]
        if j < 4:
            rows[i][j] = j ** 3  # random.random()

    ut.typewrite("\nSum row: {0:d}\n".format(sum(rows[i])))
    ut.typewrite("\nSum col: {:d}".format(sumCol))

print(rows)
