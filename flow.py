# $Id: flow.py, 4b3c476d11af  makhtar $
# Control flows and iterations with ranges

import random

x = random.randint(-20, 20)
if x < 0 :
    print (x, "is negative")
elif x > 0:
    print (x, "is positive")


for i in range(5): {
    print(i, end=" ")
}

words = ['monster', 'window', 'defenestrate']
words.sort()
for w in words:
    print("\t", w)

print("\nRange with step: ", list(range(0, 10, 3)))

print("\nIndices:")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(f"{i}: {a[i]}")

print("\n***** Checking prime numbers ....")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break

    else:
        # else not related to the previous if, but to the 'for'
        # loop fell through without finding a factor
        print(n, 'is a prime number')
