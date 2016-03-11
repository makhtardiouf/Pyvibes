
# Trivial files I/O
import sys
import os

s = "s";
fp = open("arrays.py")
print("Input a line: ")

while s:
    s = fp.readline()
    print(s)
    if s == 'q':
        break

os.close(fp)