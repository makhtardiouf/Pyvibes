# Testing bag
# Makhtar Diouf
from datetime import date
import random

print(type(3))
print(type("Hello"))

i = 1267.899
print(type(i))

a = [-5, "On it", True, 0.48, 0x123, 'Ab' + 'Cd']

for i in a:
    print("Type of", i, type(i))

print("Type of a", type(a), "\n\n")

def sequencer(*arg, sep="/"):
    return str(date.today()) + sep + sep.join(arg) + str(random.random())

print("Contract number", sequencer("CTR0123", "XXX-A"))

def cshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

