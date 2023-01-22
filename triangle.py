''' Print a triangle using asterisks '''

n = 4

for i in range(1, n + 1):
    for j in range(i):
        print("*", end='')
    print()
