# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 16:49:28 2016
Method overloading: mangles identifiers starting with "__"
https://docs.python.org/3.4/tutorial/classes.html
$Id: cloverload.py, 6a8319e303c1  makhtar $
"""
import random

class Mapping:
    def __init__(self, iterable):
        self.items = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items.append(item)

it = {"a": 1, "b":200, "c":900}

m = MappingSubclass(it)
m.update(list("z"), it.reverse())
print(m.items)
