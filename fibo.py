# $Id: fibo.py, 6a8319e303c1  makhtar $
# Module example Fibonacci numbers
__name__ = 'Test fibonacci demoing modularisation'

def fib(n):  # write Fibonacci series up to n
    print("Calculating ", n)
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

# make the file usable as a script as well as an importable module
# test as python fibo.py 10
#if __name__ == "__main__":
import sys

print(fib2(int(sys.argv[1])))
