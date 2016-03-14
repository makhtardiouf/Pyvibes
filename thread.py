

import threading, zipfile
import os

class AsyncZip(threading.Thread):

    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        print("zipping file in the background")
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished creating zip', self.outfile)

os.system("touch pydata.txt")
bgThread = AsyncZip('pydata.txt', 'pyarchive.zip')
bgThread.start()
print('The main program continues to run in foreground.')

bgThread.join()    # Wait for the background task to finish

# Better design:  concentrate all access to a resource in a single thread and
# then use the Queue module to feed that thread with requests from other threads.
