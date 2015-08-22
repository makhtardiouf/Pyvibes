__author__ = 'makhtar'

# https://docs.python.org/3/tutorial/controlflow.html
# Small anonymous function create uses a lambda expression to return a function. Another use is to pass a small function as an argument:
# with parameter annotation

def increm(n: int):
    print("Annotations:", increm.__annotations__)
    return lambda x: x + n


f = increm(42)
print(f(0))
