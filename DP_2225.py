n, m = map(int,input().split())
dp = [[0 for _ in range(n+1)] for _ in range(m)]
for i in range(n+1):
    dp[0][i] = 1
for i in range(m-1):
    for j in range(n+1):
        for k in range(j+1):
            dp[i+1][j] += dp[i][k]
            dp[i+1][j] %= 1000000000
print(dp[m-1][n])