
# $Id: queuedemo.py, db96579442c0  makhtar $
# https://docs.python.org/3.4/tutorial/datastructures.html
# FIFO, designed to have fast appends and pops from both ends

from collections import deque

queue = deque(["Elhadji", "Johana", "Mouhammad"])
print(queue)
queue.append("Jimmy")  # Terry arrives
queue.append("Ibrahim")  # Ibrahimovich arrives

print(queue)

queue.popleft()  # The first to arrive now leaves
print(queue)
queue.reverse()
print(queue)
