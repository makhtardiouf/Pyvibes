#!/usr/bin/env python3
"""
Parse a file containing ASN1 pseudo-code and prep it for C++ conversion. Shares some similarities with asn1c, but this version focus on the latest 3GPP TS docs extraction.

Formats the output file with 'astyle'.
$Id: asn1convert.py, 9ddcffa7b4df  makhtar $
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
    "ENUMERATED": " enum ",
    "BOOLEAN": " bool ",
    "INTE": " int ",
    "STRING": " string ",
    "OPTIONAL": '',
    "Need ON": " ",
    "Need OP": " ",
    "NULL": 'typedef ',
    "...": "\n\n",
    "[[": " \n",
    "]]": " \n",
    "::=": " ",
    #"--": " // ",
    "-": '',
    ",": ' ',
    "\t": ''
}

try:
    line = fp.readline()
    outp = open(fp.name + ".h", "w")
    # Foward declarations header file
    outp2 = open(fp.name + "_typedefs.h", "w")
    outp.write('#include "' + outp2.name + '"\n')

    typedef_list = []
    inAsn = False

    def checkAsn(_line):
        global inAsn
        global line
        if "ASN1START" in _line:
            inAsn = True
            outp.write("// " + _line.strip() + "\n")
            line = fp.readline()

        elif "ASN1STOP" in _line:
            inAsn = False
        return inAsn

    while line != '':
        inAsn = checkAsn(line)
        if not inAsn:
            # Comment out non-ASN text
            outp.write("// " + line.strip() + "\n")
            line = fp.readline()
            continue

        tmp = line.split("\t")
        parts = [str(_).strip() for _ in tmp]
        del(tmp)
        line = ''

        for s in reversed(parts):
            s = s.strip()
            if s.isspace():
                continue
            elif ('(' not in s):
                line += s.strip() + " "
            else:
                # e.g. INTEGER (0..28)
                line += (s[:4]) + " "

        d1 = False
        d2 = False
        d3 = False  # struct in previous line

        if "{" in line:
            d1 = True
            line = re.sub("{", " ", line)
            line = str(line) + " {"

        elif "}" in line:
            d2 = True
            line = "\t" + str(line)
        elif "struct" in line:
            d3 = True
            line = "\t" + str(line)

        # Replace items present in the symbols table
        for k in opts:
            if k not in line:
                continue
            line = re.sub(re.escape(k), opts[k], line.strip())

        if not line.isspace():
            if ("bool" not in line) and ("int" not in line):
                s = line.split(' ')
                d = d1 or d2 or d3
                i = 0
                typed = s[i]
                while typed.isspace():
                    typed = s[i]
                    i += 1

                if (not d) and not (typed == "typedef"):
                    typedef_list.append(typed)
                del(s)

        if d1:
            outp.write("\t" + line + "\n")
        else:
            outp.write("\t" + line + ";\n")
        line = fp.readline()

except Exception:
    print("Aborting, regex error ", sys.exc_info()[0])
    # raise

finally:
    fp.close()
    os.system("astyle --style=gnu " + outp.name)
    print("See output file: ", outp.name)

    outp2.write("\n// Forward declarations for " + outp.name)
    outp.close()
    for s in typedef_list:
        outp2.write("\ntypedef " + s + ";")
    outp2.close()
