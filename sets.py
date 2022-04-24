

# $Id: sets.py, c86448423bdc  makhtar $
# set: unordered collection with no duplicate elements
# support mathematical operations like union, intersection, difference, and symmetric difference

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

print('orange' in basket)  # fast membership testing

a = set('abracadabra')
b = set('alacazam')
print('\n', a)  # unique letters in a
#{'a', 'r', 'b', 'c', 'd'}
print('\n', b)

print('\n', "a - b", a - b)  # letters in a but not in b
# {'r', 'd', 'b'}
print('\n', "a | b",  a | b)  # letters in either a or b
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

print('\n', "a & b",  a & b)  # letters in both a and b
# {'a', 'c'}
print('\n', "a ^ b",  a ^ b)  # letters in a or b but not both

# Sets comprehension

a = {x for x in 'abracadabra' if x not in 'abc'}
print('\n', a)


def count_substring(s, sub):
    '''Count substring, including overlap '''
    found = set()
    for i in range(len(s)):
        found.add(s.find(sub, i))
        print(f"Index: {i}, Set: {list(found)}")

    return len([x for x in found if x >= 0 ])

print(count_substring("ininini", "ini"))