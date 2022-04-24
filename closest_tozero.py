
'''
Find the temperature that is closes to 0
'''

def closestToZero(ts: list):
    if((len(ts) == 0) or (0 in ts)):
        return 0

    negatives = sorted([x for x in ts if x < 0])
    left = float('-inf')
    if len(negatives) > 0:
        left = max(negatives)
    
    positives = sorted([x for x in ts if x > 0])
    right = float('inf')
    if len(positives) > 0:
        right = min(positives)

    if abs(left) < right:
        return left
    return right

data = [-273] #[7, -10, 13, 8, 4, -7.2, -12, -3.7, 3.5, -9.6, 6.5, -1.7, -6.2, 7]
res = closestToZero(data)

print("Input temperatures: ", sorted(data))
print(f"Closest to 0: {res}")
