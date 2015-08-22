__author__ = 'Makhtar'

# for use such methods to iterate over sequences

class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Using Generators is more compact
def gen_reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


test = Reverse("abcd")
iter(test)

for ch in test:
    print(ch)

for ch in gen_reverse("abcd"):
    print(ch)
