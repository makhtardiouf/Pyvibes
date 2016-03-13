
# Dictionnaries = “associative arrays”, indexed by keys,
# https://docs.python.org/3.4/tutorial/datastructures.html
# $Id: dict.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
import datetime as dt

contact = {"name": "Makhtar", "last_name": "Diouf", "tel": +12145672, "address": "Galsene sur scene",
           "registration": dt.datetime.now()}

for key in sorted(contact):
    print(str(key).capitalize(), ":", contact[key])

# Similar to
for k, v in contact.items():
     print(str(k).capitalize(), ":", v)

print("tel" in contact, list(contact.keys()))

# builds dictionaries directly from sequences of key-value pairs
d =  dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)

# See keyvalues.py

