'''
You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to.
Sample: 
Input 1 1 1 2  (one per line)
Output [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    arr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]  

    print(arr)

