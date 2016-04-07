#!/usr/bin/env python3
"""
Parse a file containing ASN1 pseudo-code and prep it for C++ conversion
$Id: asn1convert.py, ca5aafa57b53  makhtar $
"""
import sys
import os
import re

__author__ = "Makhtar Diouf"

inp = ''
if len(sys.argv) < 2:
    # input("Specify the ASN file to convert: ")
    inp = "asn1test.txt"
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
    "OPTIONAL": '',
    "Need ON": " ",
    "Need OP": " ",
    "NULL": '',
    "...,": "\n\n",
    "[[": " \n",
    "]]": " \n",
    "::=": " ",
    "--": " // ",
    "-": '',
    ",": '',
    "\t": " "
}

try:
    line = fp.readline()
    outp = open(fp.name + ".h", "w")
    dest = ""
    while (line != ''):
        # if not line: break
        tmp = line.split("\t")
        parts = [str(_).strip() for _ in tmp]
        line = ''
        for s in reversed(parts):
            s = s.strip()
            if (s == " ") or (s == "\t"):
                continue
            line += s + " "

        d1 = False
        d2 = False
        d3 = False  # struct in previous line
        EOL = "; "
        for k in opts:
            if k not in line:
                continue

            if "{" in line:
                d1 = True
                line = re.sub("{", " ", line)
            elif "}" in line:
                d2 = True
            elif "struct" in line:
                d3 = True
                #EOL = ";"

            line = re.sub(k, opts[k], line) + " "

        if d1:
            line = str(line) + " { "

        elif d2:           
            line = "\t" + str(line) + " "

        elif "}" not in line:
            line = "\t typedef " + str(line) + EOL

        else:
            line = "\t}"
            if d3:
                line += ";"

        outp.write(line + "\n")
        line = fp.readline()

except Exception:
    print("Aborting, regex error ", sys.exc_info()[0])
    
finally:
    fp.close()
    outp.close()
    print("See output file: ", outp.name)
