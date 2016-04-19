#!/usr/bin/env python3
"""
Plot RSRP of UEs
Loads the data in a brute force fashion
Run it from directory where the data file is located
Makhtar Diouf
$Id$
"""
import os, sys
import numpy as np
from matplotlib import pyplot as plt
import operator

file = "DlRsrpSinrStats.txt"
if len(sys.argv) > 1:
    file = sys.argv[1]
stats = file.split('.')[0]

if not os.path.exists(file):
    print("Could not find the LTE data stats, verify the path of: ", file)
    sys.exit()

print("Loading data from", file, " please wait...")
data = np.loadtxt(file, dtype=float, comments='%')

Time, CellId, IMSI, RNTI, RSRP, RSRP_dBm, Sinr, SINR_dB = data.T

plt.xlabel("Time (s)")
plt.ylabel("SINR (dB)")
plt.title(" SINR vs Time (" + stats + ")")

UES = [2,5]

def plotUe(imsi = 1):
    sinr = [0] * len(RSRP_dBm)
    times = [0] * len(sinr)
    i, j = 0, 0
    
    for ue in IMSI:
        if IMSI[i] == imsi:
            #print(i, j, IMSI[i], RSRP_dBm[i])
            sinr[j] = SINR_dB[i]
            times[j] = Time[i]
            j += 1
        i += 1
    plt.plot(times, sinr)
    

for i in UES:
    plotUe(i)

plt.legend(UES)
fname = stats + ".svg"
plt.savefig(fname)
print("See image", fname)
