''' 
 Base conversions in a specific width

 '''

def printBases(number):
    w = len(format(number, 'b'))
        
    for i in range(1, number+1):
        print(f"{i}".rjust(w), f"{i:o}".rjust(w), f"{i:X}".rjust(w), f"{i:b}".rjust(w))

if __name__ == '__main__':
    n = int(input("Enter a number to convert: "))
    printBases(n)


