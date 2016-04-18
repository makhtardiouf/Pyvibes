#!/usr/bin/env python3
"""
Codejam 20160416 R1A
Makhtar Diouf
Problem A: The Last Word (after permutating a string)
$Id$

wins if their last word is the last of an alphabetically sorted list of all of the possible last words that could have been produced

"""
import sys
from itertools import permutations, combinations

# Not necessary
def permutate(s):
    l = list(S)
    perms = [''.join(p) for p in permutations(l, len(l))]    
    perms2 = sorted(perms, reverse=False)
    return perms2[-1]


def solve(S):  
    q = ''
    for i in range(0, len(S)):
        q = max(S[i] + q, q + S[i])
                
    return q


#### main
try:
    file = "A-large-practice.in" #"A-test.in" 
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')
    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for c in range(1, nCases + 1):
        S = inp.readline().strip()
        print("S:", S)

        line = "Case #{}{}{}\n".format(c, ': ', solve(S))
        sys.stdout.write(line)
        outp.write(line)


except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()

