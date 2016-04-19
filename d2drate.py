#!/usr/bin/env python3
"""
Plot data rates of D2D UEs
Loads the data in a brute force fashion
Run it from directory where the data file is located
Makhtar Diouf
$Id$
"""
import os, sys
import numpy as np
from matplotlib import pyplot as plt
import operator

file = "DlPdcpStats.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]
stats = file.split('.')[0]

if not os.path.exists(file):
    print("Could not find the LTE data stats, verify the path of: ", file)
    sys.exit()

print("Loading data from", file, " please wait...")
data = np.loadtxt(file, dtype=float, comments='%')

# Forced to unpacked all fields
start, end, CellId, IMSI, RNTI, LCID, nTxPDUs, TxBytes, nRxPDUs, RxBytes, delay, stdDev, minD, maxD, PduSize, stdDev, minD2, maxD2 = data.T

#print(start.__class__, IMSI.__class__, RxBytes.__class__)
plt.xlabel("Time (s)")
plt.ylabel("Throughput (Mbit/s)")
plt.title(" CUE Throughput vs Time (" + stats + ")")
#plt.hold()

CUES = [2,5]

def plotUe(imsi = 1):
    ueRate = [0] * len(RxBytes)
    times = [0] * len(ueRate)
    i, j = 0, 0
    
    for rxB in RxBytes:
        if IMSI[i] == imsi:
            #print(i, j, IMSI[i], RxBytes[i])
            ueRate[j] = rxB / (1e6 * 0.25)
            times[j] = start[i]
            j += 1
        i += 1
    plt.plot(times, ueRate)
    

for i in CUES:
    plotUe(i)

def setLegend(i):
    return "CUE" + str(i)

plt.legend(CUES)  # map(setLegend, CUES))

# Formats available: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
fname = stats + ".svg"
plt.savefig(fname)
print("See image", fname)

#plt.show()

