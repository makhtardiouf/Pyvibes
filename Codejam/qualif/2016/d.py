#!/usr/bin/env python3
# Codejam 20160408
# Makhtar Diouf
# $Id$
# Problem D:
import sys

def processtls(tiles):
    if isinstance(tiles, list):
        return ' '.join(map(str, tiles))
    return tiles

def checktiles(orig, iters, numsampling):
    if numsampling > orig:
        return 'IMPOSSIBLE'

    if numsampling == orig:
        chktiles = [x + 1 for x in range(numsampling)]
        return chktiles

    if numsampling == orig - 1:
        if iters == 1:
            return 'IMPOSSIBLE'

        chktiles = [x + 2 for x in range(numsampling)]
        return chktiles
    return 'IMPOSSIBLE'

def solve(line):
    orig, iters, nsampling = tuple(map(int, line.split(' ')))
    tiles = checktiles(orig, iters, nsampling)
    return processtls(tiles)

# main
try:
    file = "D-large.in"
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')

    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for k in range(1, nCases + 1):
        line = inp.readline().strip()
        print("line:", line)

        line = "Case #{}{}{}\n".format(k, ': ', solve(line))
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()
