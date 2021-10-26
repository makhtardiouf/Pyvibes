#!/usr/bin/python3
""" Test file reading """
import os, sys

if len(sys.argv) < 2:
    print(f"Usage {sys.argv[0]} [FILENAME]")
    sys.exit(0)

target = sys.argv[1]
if not os.path.isfile(target):
    print(f"File {target} not found in the specified path");
    sys.exit(0);

try:
    print(f"{'-' * 10}Reading file {target}...")
    with open(target) as fp:
        n = 0
        for line in fp:
            if len(line) > 1:
                print(line)
                n += 1

        print(f"{'-' * 10}Done reading {n} non-empty lines")

except Exception as e:
    print(f"Error processing file {target}: {e}")