# $Id: flow.py, 4b3c476d11af  makhtar $
# Control flows and iterations with ranges

import sys
import random

x = random.random()
if x < 0 :
    print (x, "is negative")
elif x > 0:
    print (x, "is positive")


a = ""
for i in range(5): {
   # a = str.format("{} {}", "1", i)

    print (i)
}

words = ['monster', 'window', 'defenestrate']
words.sort()
for w in words:
    print(w)

print("Range with step: ", list(range(0, 10, 3)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break

    else:
        # else not related to the previous if, but to the 'for'
        # loop fell through without finding a factor
        print(n, 'is a prime number')
