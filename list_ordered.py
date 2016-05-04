# OrderedList implementation
# Data structure streamlined and augmented by Makhtar Diouf
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html
from random import randint


class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    # Operator overloading (>)    
    def __gt__(self, Node):
        return self.data > Node.data

# Inherit list()
class OrderedList(list):

    def __init__(self):
        self.head = None
        self.idx = 0
        self.sz = 0

    def index(self, item):
        exists = self.search(item)
        if exists:
            return self.idx
        return None

    def search(self, item):
        self.idx = 0
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
                    self.idx += 1

        return found

    def swap(self, n1, n2):
        tmp = n1.data
        n1.data = n2.data
        n2.data = tmp
    
    def add(self, item):
        self.idx = 0
        current = self.head
        prev = None
        stop = False
        tmp = Node(item)
        while current != None and not stop:
            if current > tmp:
                stop = True
            else:
                prev = current
                current = current.next
                self.idx += 1
        
        if prev == None:
            tmp.next = self.head
            self.head = tmp
        else:
            tmp.next = current
            prev.next = tmp
            
        self.sz += 1
        self.idx += 1
        if (current) and (current.data > item):
            self.swap(current, tmp)
            self.insert(self.idx-2, item)
        else:
            self.insert(self.idx, item)

    def isEmpty(self):
        return self.head == None

    def size(self):        
        return self.sz


l = OrderedList()
l.add(150)
l.add(93)
for i in range(10):
    l.add(randint(i, 200))

print(l.size())
print(l.search(93))
print(l.search(100))
print("Deleting idx: ", l.index(93))
# del(l.index(31))
print(l.size())
print(l, "\n\n")

l = sorted(l)
for i in range(len(l)):
    print(l[i], end=', ')
print()
