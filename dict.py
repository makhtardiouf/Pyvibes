
# Dictionnaries = “associative arrays”, indexed by keys,
# https://docs.python.org/3.4/tutorial/datastructures.html
# $Id: dict.py, c86448423bdc  makhtar $
import datetime as dt

contact = {"surname": "Makhtar", "lastname": "Diouf", "phone": +12145672, "address": "Galsene sur scene",
           "registration": dt.datetime.now()}

for k, v in contact.items():
    print(str(k).capitalize(), ":", v)

print("-----------\n")

# Similar to
for key in sorted(contact):
    print(str(key).capitalize(), ":", contact[key])

print("-----------\n")
print("tel" in contact, list(contact.keys()))

# builds dictionaries directly from sequences of key-value pairs
d =  dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)

# See keyvalues.py
