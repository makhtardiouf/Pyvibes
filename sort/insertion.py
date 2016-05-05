"""
Insertion sort, O(n^2)
Maintains a sorted sublist in the lower positions of the list. 
Each new item is then “inserted” back into the previous sublist 
such that the sorted sublist is one item larger. 

http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""

def insertionSort(alist):
    for i in range(1, len(alist)):
        pos = i
        curVal = alist[i]

        while pos > 0 and alist[pos - 1] > curVal:
            alist[pos] = alist[pos - 1]
            pos = pos - 1

        alist[pos] = curVal
        print(alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)
