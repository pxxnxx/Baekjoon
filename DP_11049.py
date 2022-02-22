import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
for v in range(1, n):
    for i in range(n-v):
        j = i + v
        for k in range(v):
            dp[i][j] = min(dp[i][j], dp[i][i+k] + dp[i+k+1][j] + arr[i][0] * arr[i+k][1] * arr[j][1])
print(dp[0][n-1])