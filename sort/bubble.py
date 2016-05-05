"""
Short Bubble sort makes multiple passes through a list.
It compares adjacent items and hit those that are out of order.
Often considered the most inefficient sorting method since it must 
exchange items before the final location is known
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
"""

def bubbleSort(alist):
    hit = True
    passnum = len(alist) -1
    while passnum > 0 and hit:
        hit = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                hit = True
                # Swap the python way
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                
        passnum -= 1
        if hit:
            print("P"+str(passnum), alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Init:", alist)
bubbleSort(alist)
