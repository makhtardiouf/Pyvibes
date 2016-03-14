
# Trivial files I/O
import sys
import os

s = "s";
fp = open("arrays.py")
print("Reading file ", fp.name)

# Safe to use
# with open('workfile', 'r') as f:
    
while s:
    s = fp.readline()
    print(s)
    if s == 'q':
        break


#os.close(fp)
# equals
fp.close()
