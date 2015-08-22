__author__ = 'makhtar'

# $Id$
# Dictionaries or “associative memories” or “associative arrays”.

import random

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print('\n', tel)

# {'sape': 4139, 'guido': 4127, 'jack': 4098}

print('\n', "Jack's number is: ", tel['jack'])

del tel['sape']
print('\n', tel.values())

tel['irv'] = random.randint(5, 100)
# print('\n', sorted(tel))

print(dict(sape=4139, guido=4127, jack=4098))

for key in sorted(tel):
    print('\t', key, " -> ", tel[key])

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Retrieve position index and corresponding value
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# loop over two or more sequences at the same time, pairing the entries with zip()

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e
