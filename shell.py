__author__ = 'Makhtar'

"""
Running system commands available from the shell
"""
import subprocess
import sys

def runCmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    for line in (proc.stderr or proc.stdout):
        print(line.strip())

    retval = proc.wait()
    return retval
    #out = p.stdout.read().strip()



runCmd("dir")
