__author__ = 'makhtar'


# https://docs.python.org/3/tutorial/controlflow.html
# Small anonymous function uses a lambda expression to return a function.
# Another use is to pass a small function as an argument:
# with parameter annotation

def increm(n: int) -> int:
    print("Annotations:", increm.__annotations__)
    return lambda x: x + n


f = increm(42)
print(f(0))
print(f(1))

g = increm(2)
print(f(2) + g(3))
