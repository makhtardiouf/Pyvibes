__author__ = 'makhtar'
# $Id: queuedemo.py, 1b4d9138d63b 1457879538.0-32400 makhtar $
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
