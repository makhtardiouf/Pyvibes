__author__ = 'Makhtar'
"""
Regroup utility functions, classes, vars
$Id: utils.py, 4b3c476d11af  makhtar $
If compiled, make sure utils.so is not in the same directory as utils.py
"""
import datetime
import time
import sys
import logging
import cProfile

def __init__():
    logging.basicConfig(level=logging.DEBUG, filename=(sys.argv[0] + ".log"))


def showMsg(msg):
    print("\n", datetime.datetime.now(), msg)


def typewrite(s, sleep_t=0.05):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(sleep_t)

def logit(msg):
    logging.debug(msg)


def time_code(func, *args, **kwargs):
    from timeit import timeit as tm
    print(func, args)
    s = [ str(_) for _ in args]
    print(tm("stmt=" + func + "(" + ','. join(s) + ")", setup="from __main__ import "+func))


# Profiler
def do_cprofile(func):
    """Add @utils.do_cprofile just before the target function definition"""
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
