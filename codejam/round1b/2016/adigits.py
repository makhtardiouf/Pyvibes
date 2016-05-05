#!/usr/bin/env python3
"""
Codejam 20160430 R1B
Phone number parsing from obfuscated string
Makhtar Diouf
$Id$
"""
import sys
import re
# import os
# import math

digits = {"ZERO": "0", "ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5",
          "SIX": "6", "SEVEN": "7", "EIGHT": "8", "NINE": "9"}

class GenNumber:

    def __init__(self, S, num):
        self.S = S
        self.num = num
        self.tries = 20

    def clearSubs(self, subS):
        S = list(self.S)
        for s in subS:
            for i, s2 in enumerate(S):
                if s == s2:
                    S.pop(i)
                    break
        return ''.join(S)

    def getDigits(self):
        """Parse mixed digits, along with duplicates"""
        for k in digits:
            hit = True
            subS = list()
            for l in k:
                if l not in self.S:
                    hit = False
                    break
                else: subS.append(l)

            if hit:
                d = digits[k]
                if d == "3":
                    if self.S.count("E") >= 2:
                        self.num.append(d)
                else:
                    self.num.append(d)
                # Clear corresponding chars in S
                self.S = self.clearSubs(subS)
                
        if self.tries and ''.join(self.S).isalpha():
            print(self.S)
            self.tries -= 1
            return self.getDigits()
        return ''.join(sorted(self.num))


def solve(S):
    num = list()
    for k in digits:
        if k not in S:
            continue
        # Replace full str numbers to their digits counterpart
        S = re.sub(re.escape(k), digits[k], S)
        num.append(digits[k])

    c = GenNumber(sorted(S), num)
    return c.getDigits()

# main
try:
    file = "A-small-practice.in" # "atest.in"
    inp = open(file)
    outp = open(inp.name + ".out", mode='w')
    nCases = int(inp.readline().strip())
    print(nCases, " test cases")

    for c in range(1, nCases + 1):
        S = inp.readline().strip()
        line = "Case #{}{}{}\n".format(c, ': ', solve(S))
        sys.stdout.write(line)
        outp.write(line)

except Exception as ex:
    print("Error: ", sys.exc_info()[0], ex)
    raise

finally:
    inp.close()
    outp.close()
