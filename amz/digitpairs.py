"""
Identify pairs of integers in an array which sum to a specified x.
Use a hashtable

Makhtar Diouf, Python3
"""

data = [4, 9, 2, 3, 5, 15, 1, 7, 10, 6, 5, 0, -1, 5]
xSum = 10
hashm = {}
dbg = True

if dbg:
    print("Checking digit pairs from", data, "summing to", xSum)
    
def insertKey(inKey):
    if inKey in hashm.keys():
        cnt = hashm.get(inKey)
        hashm.update({inKey: cnt+1})
        
    else:
        hashm.update({inKey: 1})


for i in range(0, len(data)):
    a = data[i]    
    if a > xSum:         
        continue
    
    b = xSum - a
    if b in hashm.keys():
        cnt = hashm.get(b)
        if cnt > 0:
            print(a, b)
            #hashm.update({b: cnt-1})
            hashm[b] = cnt - 1
        else:
            insertKey(a)
            
    else:
        insertKey(a)

