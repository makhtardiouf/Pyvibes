__author__ = 'makhtar'

import os, sys
import numpy as np
from matplotlib import pyplot as plt

file = "/home/makhtar/Documents/Code/Wireless-src/ns3-dev/DlPdcpStats.txt"
    #repr(os.getenv('NS3_DIR')) + "/" + "DlPdcpStats.txt"

if not os.path.exists(file):
    print("Could not find the LTE data stats, verify the path of: ", file)
    sys.exit()

data = np.loadtxt(file, dtype=float, comments='%')

start, end, CellId, IMSI, RNTI, LCID, nTxPDUs, TxBytes, nRxPDUs, RxBytes, delay, stdDev, min, max, PduSize, stdDev, min, max = data.T

#plt.axes([0.2, 0.1, 0.5, 0.8])
plt.xlabel("Time (s)")
plt.ylabel("Throughput (Mbit/s)")
#plt.hold()

def plotUe(imsi = 1):
    ueRate = []
    for i in IMSI:
        if i == imsi:
            ueRate = TxBytes / (1e6 * 0.25)
            plt.plot(start, ueRate ) #, start, RxBytes / (1e6 * 0.25))

for i in IMSI:
    plotUe(i)

plt.legend((IMSI)) #, 'RxBytes'), loc=4)
plt.show()
