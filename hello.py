# $Id: hello.py, ba755c6924d3  makhtar $

import sys
import datetime as dt
from time import sleep

today = dt.date.today()
print(str.capitalize("hello python, today is") , 
      dt.datetime.strftime(today, "%A, %B %d, %Y"))
      
print("Running argv[0]: " + sys.argv[0])

msg = "Programming is just logic"
print(msg, len(msg))

words = ['monster', 'window', 'appear']
for w in words:
    print(w, w.__class__, len(w))

print("Raw string: " + r'C:\some\name')

i = 0
while i < len(msg):
    print(msg[i], end=' ')
    sleep(0.05)
    i += 1

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

print("\n", words, words.__class__)
print(isinstance(words, str), isinstance(words, list))