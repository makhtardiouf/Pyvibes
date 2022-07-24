''' Un orderred pairs in a sequences '''
import random 

def printUnorderedPair(s):
    for i in range(len(s)):
        print('\t' * i, end='')
        for j in range(i+1, len(s)):
            print(f"({i}, {j})", end=' ')
        print("")

s = [random.randint(0, 100) for x in range(8)]
printUnorderedPair(s)
