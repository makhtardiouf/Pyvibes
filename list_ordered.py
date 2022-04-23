""" OrderedList implementation
 Data structure streamlined and augmented by Makhtar Diouf
 http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html"""
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
        list.__init__(self)
        self.head = Node(0)
        self.idx = 0
        self.sz = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.sz

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
        # Python's short hand swap
        n1.data, n2.data = n2.data, n1.data


    def add(self, item):
        try:
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

            #breakpoint()
            self.sz += 1
            self.idx += 1
            #self.insert(self.index(current.data), item)
            # workaround the above bug
            self.append(item)
            self.sort()

        except Exception as e:
            print(f"Failed to add item: {e}")



orders = OrderedList()
for i in range(10):
    orders.add(randint(i, 200))

print(orders.size())
print(orders.search(93))
print(orders.search(100))

print("Deleting idx: ", orders.index(93))
# del(orders.index(31))
print(orders.size())
print(orders, "\n\n")

for i,v in enumerate(orders):
    print(orders[i], end=', ')
print()
