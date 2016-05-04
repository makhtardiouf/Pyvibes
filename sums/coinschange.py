'''Classic coin change problem,
Use Dynamic Programming to cache computed data in a memo table

Hrank: output number of ways we could make the change
https://www.hackerrank.com/challenges/coin-change'''
import sys

M, n = [int(x) for x in sys.stdin.readline().split()]
coins = [int(x) for x in sys.stdin.readline().split()]
dp = [0]*(M+1)
dp[0] = 1

for i in range(1, n+1):
    for j in range(1, M+1):
        c = coins[i-1]
        if j >= c:
            dp[j] += dp[j-c]
            
print(dp[-1])
