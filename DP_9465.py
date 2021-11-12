import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    dp = []
    for i in range(2):
        dp.append(list(map(int,input().split())))
    for i in range(1,n):
        if i == 1:
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
        else:
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))
