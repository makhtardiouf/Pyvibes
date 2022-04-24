""" Find the number closest to 0 
Sample inputs 10 / -40 -5 -4 -2 2 4 5 11 12 18
"""
import sys
import math

try:
    n = int(input("Enter the number of temperatures to analyse: "))
    print("#Items:", n, file=sys.stderr, flush=True)
    if n == 0:
        print(0)
        exit(0)

    print("Enter the list of numbers to check: ")
    temps = input().split()
    temps = [int(t) for t in temps]
    temps.sort()
    print("Sorted input: ", temps, file=sys.stderr, flush=True)

    pos_temps = map(abs, temps)
    t = min(pos_temps)
    print(t if t in temps else -t)

except Exception as e:
    print("Processing failed", e)