# $Id$

import sys
import time
from time import sleep

print(str.capitalize("hello python, it's ") + str(time.localtime()))
print("argv[0]= " + sys.argv[0])

mesg = "Programming is good"
print(mesg, len(mesg))

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print("Raw string: " + r'C:\some\name')

i = 0
while i < len(mesg):
    print(mesg[i], end=' ')
    sleep(0.5)
    i = i + 1

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print(words)
