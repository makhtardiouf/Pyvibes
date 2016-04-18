#!/usr/bin/env python3
"""
Trees 
Makhtar Diouf
$Id$
Ref: http://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html
"""

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftCh = None
        self.rightCh = None

    def insertLeft(self, newNode):
        if self.leftCh == None:
            self.leftCh = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftCh = self.leftCh
            self.leftCh = t

    def insertRight(self, newNode):
        if self.rightCh == None:
            self.rightCh = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightCh = self.rightCh
            self.rightCh = t


    def getRightChild(self):
        return self.rightCh

    def getLeftChild(self):
        return self.leftCh

    def setRoot(self, obj):
        self.key = obj

    def getRoot(self):
        return self.key


r = BinaryTree('a')
print(r.getRoot())
print(r.getLeftChild())
r.insertLeft('b')

print(r.getLeftChild())
print(r.getLeftChild().getRoot())
r.insertRight('c')

print(r.getRightChild())
print(r.getRightChild().getRoot())

r.getRightChild().setRoot('hello')
print(r.getRightChild().getRoot())
