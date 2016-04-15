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

def solve():
    pass



#### main
try:
    file = "A-test.in" #"A-small-attempt0.in
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')
    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for c in range(1, nCases+1):
        board = []
        for i in range(0,5):
            board.append(inp.readline().strip())

        line = "Case #{}{}{}\n".format(c, ': ', solve())
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()

