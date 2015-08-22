__author__ = 'makhtar'
# $Id$

from collections import deque

queue = deque(["Elhadji", "Johana", "Michael"])
print(queue)
queue.append("Terry")  # Terry arrives
queue.append("Ibrahim")  # Graham arrives
print(queue)

queue.popleft()  # The first to arrive now leaves
print(queue)
queue.reverse()
print(queue)
