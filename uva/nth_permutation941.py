#!/usr/bin/env python3
"""
Return the (N+1)th permutation of a string
Using itertools.permutations is too slow for large N

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=882
See also: http://math.stackexchange.com/questions/60742/finding-the-n-th-lexicographic-permutation-of-a-string

$Id: asn1convert.py, 9ddcffa7b4df  makhtar $
"""
import sys
from math import factorial
from itertools import permutations
from makhtar import utils

def kthperm(S, k):
    """Non-recursive k-th permutation,
    all elements in S must be unique """
    P = []
    i = 0
    S = list(S)
    while S != []:
        n = len(S)
        f = factorial(n-1)
        i = int(floor(k/f))
        print(i, k, f, n, S)
        
        if (i <= n):
            x = S[i]
            P.append(x)
            S = S[:i] + S[i+1:]

        k = k%f
    return P


#@utils.do_cprofile
def solve(S, N):
    # Brute force, horrible when N is large
    if N > 200:
        return ' '
    
    p = list(permutations(S))
    #print(N, len(p))
    if len(p) > N+1:
        return ''.join(p[N+1])
    else:
        return ''.join(p[-1])

#### main
try:
    inp = sys.stdin
    nCases = int(inp.readline().strip())
    #print(nCases, " test cases")

    for c in range(1, nCases+1):
        S = inp.readline().strip()
        N = int(inp.readline().strip())

        sys.stdout.write(solve(S, N) + "\n")

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise




