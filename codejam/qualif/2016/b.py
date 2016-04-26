#!/usr/bin/env python3
# Codejam 20160408
# Makhtar Diouf
# $Id$
# Problem B:

import sys

class Cake:
    def __init__(self, chs):
        # min number of time to maneuver
        self.y = 0
        self.S = list(chs)
        self.N = len(self.S)        
        self.bin = []
        for ch in self.S:
            if ch == '-':
                self.bin.append(0)
            else:
                self.bin.append(1)


    def countflip(self, stack):
        self.y = 0
        last = stack[0]
        
        for ch in stack:
            if ch == last:
                continue            
            self.y += 1
            last = ch

        if last == 0:
            self.y += 1         
        return self.y    
    

def solve(S):
    if '-' not in S:
        return 0

    c = Cake(S)
    c.countflip(c.bin)
    return c.y


#### main
try:
    file = "B-large.in" 
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')

    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for k in range(1, nCases + 1):
        S = inp.readline().strip()
        print("S:", S)

        line = "Case #{}{}{}\n".format(k, ': ', solve(S))
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()

