# $Id$

for i in range(5): {
    print(i)
}

print("Range with step: ", list(range(0, 10, 3)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break

    else:
        # else not related to the previous if
        # loop fell through without finding a factor
        print(n, 'is a prime number')
