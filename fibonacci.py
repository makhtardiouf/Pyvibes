# Fibonnaci numbers up to n

def fibon(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b

    print()
    return result

# Now call the defined function
output = fibon(1000)
print("The output array is: ", output)
