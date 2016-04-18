"""
Regroup utility functions, classes, vars
$Id: utils.py, 0e68eb7c9c36  makhtar $
If compiled, make sure utils.so is not in the same directory as utils.py
"""
import datetime
import time
import sys
import math
import logging
import cProfile
__author__ = 'Makhtar Diouf'

def __init__():
    logging.basicConfig(level=logging.DEBUG, filename=(sys.argv[0] + ".log"))

def showMsg(msg):
    print("\n", datetime.datetime.now(), msg)

def typewrite(s, sleeptime=0.05):
    """Slowly print a string, typewriter style"""
    for i in range(len(s)):
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(sleeptime)

def logit(msg):
    logging.debug(msg)

def hashstr(astring, tablesize):
    """Hash a string, using the ordinal value of each char in the sequence. Collisions occure with anagrams"""
    tot = sum([ord(_) for _ in list(astring)])
    return tot % tablesize

def isprime(n):
    """
    Tell if the integer n is prime.
    Tests integers d from 2 up to Dmax = sqrt(n)
    """
    Dmax = math.sqrt(n)
    if n == 2:
        return True
    elif (n % 2) == 0:
        # is even
        return False
    d = 3
    while (n % d) != 0 and (d <= Dmax):
        d += 2
    return d > Dmax

def convbase(n, base):
    """Convert an integer to a given base"""
    symbols = "0123456789ABCDEF"
    if n < base:
        return symbols[n]
    else:
        return convbase(n // base, base) + symbols[n % base]


def time_code(func, *args, **kwargs):
    """ Evaluate the runtime of a function """
    from timeit import timeit as tm
    print(func, args)
    s = [ str(_) for _ in args]
    tm("stmt=" + func + "(" + ','.join(s) + ")", setup="from __main__ import "+func)

# Profiler
def do_cprofile(func):
    """Profile a non-recursive function.
    Add @utils.do_cprofile just before the target function definition"""
    def profiled_func(*args, **kwargs):
        prof = cProfile.Profile()
        try:
            prof.enable()
            result = func(*args, **kwargs)
            prof.disable()
            return result
        finally:
            prof.print_stats()
    return profiled_func
