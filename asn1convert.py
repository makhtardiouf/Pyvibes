#!/usr/bin/env python3
"""
Parse a file containing ASN1 pseudo-code and prep it for conversion to C++
$Id: asn1convert.py, ca5aafa57b53  makhtar $
"""
import sys
import os
import re

__author__ = "Makhtar Diouf"

inp = ""
if len(sys.argv) < 2:
    # input("Specify as parameter the ASN file to convert: ")
    inp = "TempAsn.txt"
else:
    inp = sys.argv[1]

fp = open(inp)
print("Reading file ", fp.name)

# Symbols table
opts = {
    "SEQUENCE": " struct ",
    "CHOICE": " enum ",
    "BOOLEAN": " bool ",
    "INTEGER": " int ",
    "OPTIONAL": " \t// Opt",
    "Need ON": ' ',
    "Need OP": ' ',
    "...": " \n",
    "[[":  " \n",
    "]]":  " \n",
    "::=": ' ',
    "-": '',
    ",": '',
    "\t": ' '
}

i = 20
while i > 0:

    tmp = str(fp.readline()).split('\t')
    parts = [str(_).strip() for _ in tmp]
    line = ""
    for s in reversed(parts):
        if (s == ' ') or (s == '\t'):
            continue
        line += s + " "

    d1 = False
    d2 = False
    
    for k in opts:
        if k not in line:
            continue
        
        if "{" in line:
            d1 = True
            line = re.sub("{", ' ', line) + " "
        elif "}" in line:
            d2 = True
            
        line = re.sub(k, opts[k], line) + " "
        
    if d1:
        sys.stdout.write("\t " + str(line) + " { ")
    elif d2:
        sys.stdout.write("\t" + str(line) + ", ")       
    else:
        sys.stdout.write("\t typedef " + str(line) + ", ")

    print()
    i -= 1

fp.close()
