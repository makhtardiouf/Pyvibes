__author__ = 'Makhtar'
'''
Regroup utility functions, classes, vars
$Id: utils.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
'''
import datetime
import time
import sys

def showMsg(msg):
    print("\n", datetime.datetime.now(), msg)


def typewrite(s, sleeptime=0.05):
    for i in range(len(s)):
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(sleeptime)


if __name__ == "__main__" :
    typewrite("Loaded makhtar's module")
