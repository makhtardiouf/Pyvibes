__author__ = 'makhtar'
# Trivial arrays operations

import sys
import time
import random
import makhtar.utils as ut

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
# empty on
# r = [[]]

for i in range(5):
    sum = 0;
    for j in range(5):
        sum += rows[i][j]
        if (j < 4):
            rows[i][j + 1] = random.random()

    ut.typewrite("Sum row: {0:.3f} \n".format(sum))
