#!/usr/bin/env python3
"""
Codejam 20160416 R1A
Makhtar Diouf
$Id$
"""
import sys
# import os
# import math
# import numpy as np
# from scipy.optimize import minimize

# If cols and rows size are the same, t[y][x] can check cols
def solve(t, n, m):
    pass



#### main
try:
    file = "A-test.in" #"A-small-attempt0.in
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')
    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for c in range(1, nCases + 1):
        n, m = [int(x) for x in inp.readline().split(sep=' ')]
        print("n, m:", n, m)

        t = []  # [[0] * n for j in range(m)]
        # Read the rows
        for i in range(n):
            row = [int(x) for x in inp.readline().split(sep=' ')]
            t.append(row)

        line = "Case #{}{}{}\n".format(c, ': ', solve(t, n, m))
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()

