#!/usr/bin/env python3
"""
 Given a paragraph of text, write a program to find the first shortest
 sub-segment that contains each of the given k words at least once. A segment is said to be
 shorter than other if it contains less number of words.

[Uncomplete BUGGY Version!]

Makhtar Diouf
$Id$
"""
import sys
# import os
# import math

# main
try:
    inp = sys.stdin
    parag = inp.readline().strip()
    allWords = parag.split(' ')
    # Remove non-alpha chars
    i = 0
    strt = end = x = y = 0

    for w in allWords:
        j = 0
        for c in w:
            if not c.isalpha():
                w = w.replace(c, "")
                print(c, end='')
            j += 1
        # print(w)
        allWords[i] = w.lower()
        i += 1

    print(allWords)
    numWords = int(inp.readline().strip())
    print(numWords, " words")

    words = []
    for c in range(numWords):
        words.append(inp.readline().strip().lower())
    print(words)
    globLen = 10000

    emptyTarget = False
    cnt = 0
    # This would miss words like "program"
    # table[target] = allWords.count(target)
    table = dict({tgt: 0 for tgt in words})

    for w in allWords:
        # emptyTarget = all(t == 0 for t in table)
        # if not emptyTarget:
        #    y -= 1
        # else:
        for tgt in table:
            if tgt in w:
                table[tgt] += 1
                break
        print("w", w, ":\t", table)

        emptyTarget = all(val == 0 for val in table.values())
        if not emptyTarget:
            #y -= 1
            if (globLen > y - x):
                globLen = y - x
                strt = x
                end = y

            tgt = allWords[x]
            if table.__contains__(tgt):
                table[tgt] -= 1
            x += 1
        y += 1

    if (end > strt):
        for i in range(strt, end):
            print(allWords[i], end='')
    else:
        print("NO SUBSEGMENT FOUND", x, y)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise
