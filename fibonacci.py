# Fibonnaci numbers up to n

def fibon(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while b < n:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b

    print()
    return result

def fiboGenerator(n):
    ''' Use Generators instead'''
    a, b = 0, 1
    while b < n:
        yield a
        a, b = b, a+b




# Now call the defined function
n = 10
output = fibon(n)
print(f"Fibonnacy sequence of {n} is: ", output)

print("Using generators now...")
for i in fiboGenerator(n):
    print(i, end=' ')
print()
