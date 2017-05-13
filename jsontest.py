__author__ = 'Makhtar'

# Demo JSON (JavaScript Object Notation) data interchange format
# can also use the python specific 'pickle' module - albeit more insecure
import json

json.dumps([1, 'simple', 'list'])
x = range(1, 100, 2)
fp = open("jsontest.json", "r+")

for val in x:
    json.dump(val, fp)

print("Check file ", fp.name)
# decode the object again
#x = json.load(fp)
#print(x)
fp.close()
