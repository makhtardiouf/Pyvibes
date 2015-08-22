__author__ = 'makhtar'
# https://docs.python.org/3/tutorial/stdlib2.html
from string import Template

t = Template('${village}folk send $$10 to $cause.')
txt = t.substitute(village='Nottingham', cause='the ditch fund')
print(txt)

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# this will leave the txt unchanged as it won't find the keyword
txt = t.safe_substitute(d)
print(txt)

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-num %f-format):  ')
# Type in mak_%n%f
t = BatchRename(fmt)

date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


# The struct module provides pack() and unpack() functions for working with variable length binary record formats
# could use the zipfile module for the following tasks

import struct

zipinput = "/home/makhtar/.PyCharm40/config/tasks/Python.tasks.zip"
with open(zipinput, 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header


import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)-8s %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    filename=(sys.argv[0] + ".log"),
                    filemode='w')

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical(' error -- shutting down')
