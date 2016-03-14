__author__ = 'Makhtar'
"""
Regroup utility functions, classes, vars
$Id: utils.py, db96579442c0  makhtar $
If compiled, make sure utils.so is not in the same directory as utils.py
"""
import datetime
import time
import sys
import logging


def showMsg(msg):
    print("\n", datetime.datetime.now(), msg)


def typewrite(s, sleeptime=0.05):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(sleeptime)


def logit(msg):
    logging.debug(msg)
    
    
if __name__ == "__main__" :
    typewrite("Loaded makhtar's module")

    logging.basicConfig(level=logging.DEBUG, filename=(sys.argv[0] + ".log"))

                        
