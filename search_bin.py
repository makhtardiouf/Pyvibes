#!/usr/bin/env python3
"""
Classic Binary search
Makhtar Diouf
$Id$
Approx number of Items to search: n / 2^i
Complexity: O(logn), from log(n) = log(2^i). Not good for small values of n
Ref: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
"""
import sys

def binarySearch(alist, item):
    print("searching for ", item, "in", alist)
    N = len(alist)
    if N == 0 :
        sys.stderr.write(str(item) + " not found\n")
        return False

    elif N == 1:
        return item == alist[0]

    else:
        midpoint = N // 2
        if alist[midpoint] == item:
           sys.stderr.write(str(item) + " found @" + str(midpoint) + "\n")
           return True

        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

bag = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(bag, 3))
print(binarySearch(bag, 13))

# For small list just do
print("Idx:", bag.index(13))

