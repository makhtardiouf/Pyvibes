__author__ = 'Makhtar'

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
[(1, 4), (2, 5), (3, 6)]

# in conjunction with the * operator can be used to unzip a list:
x2, y2 = zip(*zip(x, y))
print(x == list(x2) and y == list(y2))
