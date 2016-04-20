
# $Id: queuedemo.py, c86448423bdc  makhtar $
# https://docs.python.org/3.4/tutorial/datastructures.html
# FIFO, designed to have fast appends and pops from both ends

from collections import deque

queue = deque(["Elhadji", "Johana", "Mouhammad"])
print(queue)
queue.append("Jimmy")
queue.append("Ibrahim")
print(queue)

queue.popleft()  # First in = First out
print(queue)
queue.reverse()
print(queue)
