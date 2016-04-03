__author__ = 'Makhtar'
"""
Regroup utility functions, classes, vars
$Id: utils.py, 61514a10e198  makhtar $
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


def typewrite(s, sleeptime=0.05):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(sleeptime)


def logit(msg):
    logging.debug(msg)
    
# Profiler
def do_cprofile(func):
    """Add @utils.do_cprofile just before the target function definition"""
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func

if __name__ == "__main__" :
    typewrite("Loaded makhtar's module")