__author__ = 'Makhtar'

# Standard library demos
# https://docs.python.org/3/tutorial/stdlib.html

import os
import stat
import shutil
import glob
import re  # Regular Expressions
import random


print("Running app from ", os.getcwd())
dir = "testdir"
try:
    if not os._exists(dir):
        os.mkdir(dir)

    mode = os.stat(dir).st_mode
    print(stat.S_ISDIR(mode))

    if not stat.S_ISDIR(mode):
        os.mkdir(dir)
    print(dir, " created with mode: ", stat.filemode(mode))

    os.rename(dir, "testdir2")
    shutil.move("testdir2", dir)

except FileExistsError:
    pass

print("Scripts in directory: ", glob.glob('*.py'))

out = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print("Mach of words starting with f: ", out)

out = random.sample(range(100), 10)
print(out)
print(random.randrange(6))

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]

pprint.pprint(t, width=30)

import locale
# The value should correspond to one available on the OS
# try locale -a  |less to list them
locale.setlocale(locale.LC_ALL, 'ko_KR.utf8')
# en_US.utf8')

x = 1234567.8
print(locale.format("%d", x, grouping=True))

conv = locale.localeconv()  # get a mapping of conventions
txt = locale.format_string("%s%.*f", (conv['currency_symbol'],
                                      conv['frac_digits'], x), grouping=True)

print(txt)
