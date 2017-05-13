__author__ = 'Makhtar'

class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, content):
        self.content = content
        self.index = len(content)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.content[self.index]

# Using Generators is more compact
def gen_reverse(content):
    # step backwards by -1 till 0
    for index in range(len(content)-1, -1, -1):
        yield content[index]


test = Reverse("abcd")
iter(test)

for ch in test:
    print(ch)

for ch in gen_reverse("abcd"):
    print(ch)
