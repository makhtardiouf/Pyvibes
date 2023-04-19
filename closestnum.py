""" Find the number closest to 0 
Simpler solution to the "Temperature closest to zero problem"

Sample inputs:
-40 -5 -4 -2 2 4 5 11 12 18
7 -10 13 8 4 -7.2 -12 1 -3.7 3.5 -9.6 6.5 -1.7 -6.2 7
-273
"""
import sys

try:
    print("Enter the list of numbers: ")
    temps = list(map(float, input().split()))
    n = len(temps) 
    if n == 0:
        print(0)
    elif n == 1:
        print(temps[0])

    else:
        temps.sort()
        print(f"Sorted {n} items: ", temps, file=sys.stderr, flush=True)

        positive_temps = list(map(abs, temps))
        hit = min(positive_temps)
        print("Closest hit: ", hit if hit in temps else -hit)

except Exception as e:
    print("Processing failed: ", e)
