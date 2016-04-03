

# $Id: tryexcept.py, c86448423bdc  makhtar $
# Exception handling

import sys

try:
    f = open(sys.argv[1])
    s = f.readline()
    i = int(s.strip())

except OSError as ex:
    print("OS error: {0}".format(ex))

except ValueError as ex:
    print("Could not convert the input to an integer, please try again. ", ex.args)

except IndexError as ex:
    print("Please specify the file from which to read input, or use /dev/stdin. ", ex)

# Wildcard for all other exceptions
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# executed if the try clause does not raise an exception
else:
    print("Done processing")
    f.close()
