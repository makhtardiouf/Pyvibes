#!/usr/bin/env python3
"""
Parse a file containing ASN1 pseudo-code and prep it for C++ conversion.
Shares some similarities with asn1c, but this version focus on the latest 3GPP TS docs extraction.

Formats the output file with 'astyle'.
Ref: http://www.itu.int/en/ITU-T/asn1/Pages/introduction.aspx
Reviewed-by: Makhtar Diouf <makhtar.diouf@gmail.com>
$Id: asn1convert.py, 9ddcffa7b4df  makhtar $
"""
import sys
import os
import re

__author__ = "Makhtar Diouf"

infile = ''
if len(sys.argv) < 2:
    # input("Specify the ASN file to convert: ")
    infile = "asn1test.txt"
else:
    infile = sys.argv[1]

inp = open(infile)
print("Reading file ", inp.name)

# Symbols table
opts = {
    "SEQUENCE": " struct ",
    "CHOICE": " enum ", # verify
    "ENUMERATED": " enum ",
    "BOOLEAN": " bool ",
    "BIT": "std::bitset<1>",
    "INTE": " int ",
    "STRING": " string ",
    "OPTIONAL": '',
    "Need ON": " ",
    "Need OP": " ",
    "NULL": 'typedef ',
    "END": '// END',
    "...": "\n\n",
    "[[": " \n",
    "]]": " \n",
    "::=": " ",
    "--": " // ",
    "-": '',
    ",": ' ',
    "\t": ''
}

try:
    line = inp.readline()
    outp = open(inp.name + ".h", "w")
    # Foward declarations header file
    outp2 = open(inp.name + "_typedefs.h", "w")
    outp.write('#include "' + outp2.name + '"\n')

    typedef_list = []
    inAsn = False

    def checkAsn(_line):
        global inAsn
        global line
        if "ASN1START" in _line:
            inAsn = True
            outp.write("// " + _line.strip() + "\n")
            line = inp.readline()

        elif "ASN1STOP" in _line:
            inAsn = False
        return inAsn

    #d1 = False
    while line != '':
        inAsn = checkAsn(line)
        if not inAsn:
            # Comment out non-ASN text
            outp.write("// " + line.strip() + "\n")
            line = inp.readline()
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

        # Enum in previous line
        #if d1:
        #    opts[','] = ','

        d1 = False
        d2 = False
        d3 = False  # struct in previous line

        if "{" in line:
            d1 = True
            if 'ENUMERATE' in line:
                opts[','] = ','

            # Handle long enums, and structs
            tmp = line.split("{")
            line = tmp[0]
            tmp = tmp[1].split(',')
            if 'SEQ' in line:
                line += tmp[len(tmp)-1] + " { \n"
            else:
                line += tmp[len(tmp)-1] + " { \n\t" + tmp[0] + ", "

            line += ', '.join(tmp[1:len(tmp)-2])

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
        line = inp.readline()
        # Reset d1
        opts[','] = ' '

except Exception:
    print("Aborting, regex error ", sys.exc_info()[0])
    #raise

finally:
    inp.close()
    os.system("astyle --style=gnu " + outp.name)
    print("See output files: ", outp.name, outp2.name)

    outp2.write("\n\n// Forward declarations for " + outp.name)
    outp2.write("\n// Author: " + __author__)
    outp.close()

    for s in typedef_list:
        outp2.write("\ntypedef " + s + ";")

    # Remove empty typedefs
    outp2.close()
    os.system("sed -i 's/typedef ;/ /g' " + outp2.name)
    os.system("sed -i 's/     / /g' " + outp2.name)
    print(len(typedef_list), " typedefs generated. Check if any are missing")
    
