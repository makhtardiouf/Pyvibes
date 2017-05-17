
"""
Fibonacci Factor

Given a number K, find the smallest Fibonacci number ( other than 1 ) that shares a common factor with it. 
A number is said to be a common factor of two numbers if it exactly divides both of them. 

Output two separate numbers, F and D, where F is the smallest fibonacci number and D is the 
smallest number other than 1 which divides K and F.
Makhtar Diouf, Python3

[ Includes some bugs; pass 4/9]
"""

import os
import sys
import math

dbg = True

def fibo(k):
    """Calc F smallest Fibonacci number of k"""
    a, b = 0, 1
    d = 0
    result = []
    while a <= k:        
        # F = a
        if a > 1 :
            result.append(a)
            d = getDivisor(a, k)
            if d > 1:
                return '{}{}{}'.format(a, ' ', d)
            
        a, b = b, a + b
    return "None"


def getDivisor(f, k) :        
    # Determine D
    for d in range(2, f+1):
        if ((f % d) == 0) and ((k % d) == 0):
            return d
    return 0

# main
try: 
    print ("Fibonacci Factor; awaiting input, (see sample in fibofact.in.txt):")
    
    inp = open("fibofact.in.txt") # sys.stdin # 
    if dbg:
        outp = open("fibo.out.txt", mode='w')

    nCases = int(inp.readline().strip()) # T
    if dbg: 
        print(nCases, " test cases")

    for c in range(nCases):
        k = int(inp.readline().strip())
        if dbg:
            print("\nk:", k, end='\n')
            print("Output >")

        line = fibo(k) + "\n"
        sys.stdout.write(line)
        if dbg:
            outp.write(line)

    if dbg: 
        inp.close()
        outp.close()
    # wait on windows            
    #    inp.readline()

except Exception as ex:
    print("Error: ", sys.exc_info()[0])    
    raise
