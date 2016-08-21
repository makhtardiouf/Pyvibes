#!/usr/bin/env python3
"""
Processing a Parag of Text
[Uncomplete BUGGY Version!!]

Makhtar Diouf
$Id$
"""
import sys
# import os
# import math

def solve():
    pass



#### main
try:
    inp = sys.stdin
    
    parag = inp.readline().strip()
    allWords = parag.split(' ')
    # Remove non-alpha chars
    i = 0 
    for w in allWords:
        j = 0
        for c in w:
            if not c.isalpha():
                w = w.replace(c, "")
                print(c, end='')            
            j += 1
        # print(w)
        allWords[i] = w
        i += 1

    print(allWords)
    numWords = int(inp.readline().strip())
    print(numWords, " words")

    words = []
    for c in range(numWords):
        words.append(inp.readline().strip().lower())
    print(words)

    m = dict({"0": []})
    i = 0 # segment
    segWords = []
    segLen = 0
    curNwords = 0        
    
    for w in allWords:
        for targetW in words:
            if targetW in w.lower():
                curNwords += 1
                break

        # all words are present in segment 
        if curNwords == numWords:
            # Segment completed
            m[i] = segWords
            print(segWords)
            curNwords = 0
            segWords = []
            segLen = 0
            i += 1
        
        segWords.append(w)
        segLen += 1

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

