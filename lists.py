
#$Id: lists.py, c86448423bdc  makhtar $
# https://docs.python.org/3.3/tutorial/datastructures.html
# Lists can be used as a stack datastructure

print(f"{'-'*10} List datastructure demo {'-'*10}")
a = [66.25, 33, 33, 1, 24]
print(a)

# count returns the number of times the item appears
print("\nNumber of times an iteam appears in the list:")
print(a.count(33), a.count(66.25), a.count('x'))
m = map(a.count, a)

print(f"\nMapped count of each item:")
for x in m:
    print(f" {x}", end=" ")

print("\nInsert and append items:")
a.insert(2, -1)
print(a)
a.append(33)
print(a)
print(a.index(33))
print(a.count(33))

a.remove(33)
print(a)

print("\nReverse and sort:")
a.reverse()
print(a)
a.sort()
print(a)

squares = [x ** 2 for x in range(10)]
print(f"Squares:\n{squares}")

# Removing an item that doesn't exist is a sin
# a.remove(0)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose rows to columns
print("\nTransposing list: \n", matrix)
print(list(zip(*matrix)))

# remove an item from a list given its index
print("Removing items and slices:")
del (a[0])
print(f"\n{a}")

del (a[2:4])
print(f"\n{a}")

print("Empty list:")
a.clear()
print(f"Size of a {len(a)}")