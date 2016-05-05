"""
Selection sorted
For every pass through the list, look for the largest value and make only one exchange. 
"""
def selectionSort(alist):
    for targetSlot in range(len(alist) - 1, 0, -1):
        maxPos = 0
        for loc in range(1, targetSlot + 1):
            if alist[loc] > alist[maxPos]:
                maxPos = loc

        # Swap the python way
        alist[maxPos], alist[targetSlot] = alist[targetSlot], alist[maxPos]
        print(alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
