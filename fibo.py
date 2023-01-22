# $Id: fibo.py, 6a8319e303c1  makhtar $
# Module example Fibonacci numbers
__name__ = 'Test fibonacci demoing modularisation'

def fib(n):
    ''' Generate Fibonacci series up to n '''
    print(f"Calculating Fibonacci of {n}")

    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    ''' Generate Fibonacci array up to n '''
    print(f"Fibonnaci array of {n}")

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def recurseFibo(n):
    ''' Nth Fibonacci number '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return recurseFibo(n-1) + recurseFibo(n-2)

def memoizationFibo(n):
    '''Use a memo table to pre-compute'''
    pass

# make the file usable as a script as well as an importable module
#if __name__ == "__main__":
import sys

n = 0
if len(sys.argv) <= 1:
    n = int(input("Input a number to determine its Fibonacci serie: "))
    fib(n)
else:
    n = int(sys.argv[1])
    serie = fib2(n)
    print(serie)

print(f"{n}th Fibonacci number...")
print(recurseFibo(n))
