#!/usr/bin/env python3
"""
Find a min number of coins to give back to a client as change
Uses caching/memoization and Dynamic Programming
Makhtar Diouf
$Id$
"""
from makhtar import utils
from timeit import timeit

#@utils.do_cprofile
def probmin_coins(coinsList, change, known):
    minCoins = change
    if change in coinsList:
        known[change] = 1
        return 1

    elif known[change] > 0:
        return known[change]

    else:
        for i in [c for c in coinsList if c <= change]:
            numCoins = 1 + probmin_coins(coinsList, change - i,
                                         known)

            if numCoins < minCoins:
                minCoins = numCoins
                known[change] = minCoins
    return minCoins

# With Dynamic prog
def dp_min_coins(coinsList, change, minCoins=[0] * 64):
    for cents in range(change + 1):
        nCoins = cents
        for j in [c for c in coinsList if c <= cents]:
            if minCoins[cents - j] + 1 < nCoins:
                nCoins = minCoins[cents - j] + 1
            minCoins[cents] = nCoins
    return minCoins[change]


coinsList = [1, 5, 10, 25]
print(probmin_coins(coinsList, 63, [0] * 64))
print(dp_min_coins(coinsList, 63))
#utils.time_code("dp_min_coins", coinsList, 63)
