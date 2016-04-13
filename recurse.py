#
# Recursivity timing test
# $Id$
import random
from timeit import timeit as tm
#from makhtar import utils as ut

def getsum(numlist):
    tot = 0
    for n in numlist:
        tot += n
    return tot

# With recursion, but slower!
def resum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    return numlist[0] + resum(numlist[1:])

l = [x for x in range(20)]

print(l, tm("stmt=getsum(l)", setup="from __main__ import getsum, l"))

print(l, tm("stmt=resum(l)", setup="from __main__ import resum, l"))
