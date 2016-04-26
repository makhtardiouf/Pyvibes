#!/usr/bin/env python3
# Codejam 20160408
# Makhtar Diouf
# $Id$
# Problem C

import sys

def find_a_factor(value):
    """return a factor of a composite number, or 1 if prime"""
    for factor in range(2, int(math.sqrt(value)) + 1):
        if value % factor == 0:
            return factor

    return None

def solve(t, n, m):
    print("hello")
    pass



#### main
try:
    file = "c-test.in" #"C-small-practice.in"
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')

    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for k in range(1, nCases + 1):
        n, j = [int(x) for x in inp.readline().split(sep=' ')]
        print("n, j:", n, j)

        t = []
        # Read the rows
        for i in range(n):
            row = [int(x) for x in inp.readline().split(sep=' ')]
            t.append(row)

        line = "Case #{}{}{}\n".format(k, ': ', solve(t, n, j))
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()

