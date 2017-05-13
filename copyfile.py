__author__ = 'Makhtar'
"""
Demo R/W files
$Id$
"""
import sys

try:
    fp = open(sys.argv[1], 'r')
    if (not fp.seekable()):
        fp = open(sys.stdin, 'r')
        print("No input file specified, waiting for keyboard input: ")

    out = open(str(fp.name + "-copy.txt"), 'w')
    for line in fp:
        print("Copying line: ", line)
        out.write(line)

except (IndexError, FileNotFoundError, TypeError) as ex:
    print("Error, make sure an input file is specified", ex.args)

# clean-up actions that must be executed under all circumstances
finally:
    print('Goodbye~')
