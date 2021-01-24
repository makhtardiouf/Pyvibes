
#$Id: lists.py, c86448423bdc  makhtar $
# https://docs.python.org/3.3/tutorial/datastructures.html
a = [66.25, 33, 33, 1, 1234.5]

# count returns the number of times the item appears
print(a.count(33), a.count(66.25), a.count('x'))
m = map(a.count, a)

a.insert(2, -1)
print(a)
a.append(33)
print(a)
print(a.index(33))
print(a.count(33))

a.remove(33)
print(a)

a.reverse()
print(a)
a.sort()
print(a)

squares = [x ** 2 for x in range(10)]
print(squares)

# Removing an item that doesn't exist is a sin
# a.remove(0)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose rows to columns
print("\nTransposing list: ", matrix)
print(list(zip(*matrix)))

# remove an item from a list given its index
del (a[0])
print("\n", a)

del (a[2:4])
print("\n", a)
