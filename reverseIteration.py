''' Iterators and Generators '''
import time
__author__ = 'Makhtar'

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, content):
        self.content = content
        self.idx = len(content)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == 0:
            raise StopIteration
        self.idx -= 1
        return self.content[self.idx]

# Using Generators is more compact
''' Generators don't keep an entire serie in memory.
Results are computed on-demand. '''
def gen_reverse(content):
    # step backwards by -1 till 0
    for i in range(len(content) - 1, -1, -1):
        yield content[i]

content = "abcd"
print("Reversing the following string in two ways: ")
for c in content:
    print(c, end=' ', flush=True)
    time.sleep(0.5)

print("\n")
test = Reverse(content)
iter(test)

for ch in test:
    print(ch, end=' ')
print("\n")

for ch in gen_reverse(content):
    print(ch, end=' ')
print("\n")
