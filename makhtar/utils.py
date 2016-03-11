__author__ = 'Makhtar'
'''
Regroup utility functions, classes, vars
$Id$
'''
import datetime
import time
import sys

def showMsg(msg, a='', b=''):
    print("\n", datetime.datetime.now(), msg)


def typewrite(s):
    for i in range(len(s)):
        #print(s[i], end='')
        sys.stdout.write(s[i])
        sys.stdout.flush()
        time.sleep(0.1)


typewrite("Hello")