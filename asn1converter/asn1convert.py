#!/usr/bin/env python3
"""
Parse a file containing ASN1 pseudo-code and prep it for C++ conversion.
Formats the output file with 'astyle'
$Id: asn1convert.py, 6a8319e303c1  makhtar $
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
    "INTE": " int ",
    "OPTIONAL": '',
    "Need ON": " ",
    "Need OP": " ",
    "NULL": '',
    "...": "\n\n",
    "[[": " \n",
    "]]": " \n",
    "::=": " ",
    #"--": " // ",
    "-": '',
    ",": '',
    "\t": ''
}

try:
    line = fp.readline()
    outp = open(fp.name + ".h", "w")
    inAsn = False
    while (line != ''):

        # Is it a comment line
        cmt = re.match(re.escape("--"), line.strip())
        if cmt or (not inAsn):
            line = "// " + line.strip()
            outp.write(line + "\n")
            line = fp.readline()

            if "ASN1START" in line:
                inAsn = True
                line = fp.readline()
            else:
                continue

        if "ASN1STOP" in line:
            inAsn = False
            line = fp.readline()
            continue

        elif inAsn:
            tmp = line.split("\t")
            parts = [str(_).strip() for _ in tmp]
            line = ''
            skip = False
            for s in reversed(parts):
                s = s.strip()
                if (s == " ") or (s == "\t"):
                    continue
                if  (')' not in s):
                    line += s + " "
                else:
                    # e.g. INTEGER (0..28)
                    line += (s[:4]) + " "

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

                line = re.sub(re.escape(k), opts[k], line.strip())

        if d1:
            line = str(line) + " {"

        elif d2:
            line = "\t" + str(line)

        elif (not d2) and (not line.isspace()):
            if "bool" not in line:
                line = "\t typedef " + str(line) + EOL
            else:
                line = "\t" + str(line) + EOL

        else:
            line = "\t}"
            if d3:
                line += ";"

        outp.write(line + "\n")
        line = fp.readline()

except Exception:
    print("Aborting, regex error ", sys.exc_info()[0])
    #raise

finally:
    fp.close()
    outp.close()
    os.system("astyle " + outp.name)
    print("See output file: ", outp.name)
