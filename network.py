__author__ = 'Makhtar'

import smtplib
import urllib.request
import urllib.error

#from urllib import *

try:

    with urllib.request.urlopen('http://www.google.com/?search=makhtar') as response:
        for line in response:
            line = line.decode('utf-8')  # Decoding the binary data to text.
           # if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

    server = smtplib.SMTP('localhost')
    src = "makhtar@softandsys.com"
    dest = 'elmakdi@gmail.com'
    server.sendmail(src, dest,
                    """To: elmakdi@gmail.com
                    From: makhtar@softandsys.com

                    Hello, from Python. Remember that programming is your best bet!
                    """)
    server.quit()

except TimeoutError:
    print("Timeout, check the network connection and retry")

except urllib.error.URLError:
    print("The provided url is invalid")
