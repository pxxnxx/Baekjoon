import sys
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    sum = [0]
    for x in arr:
        sum.append(x + sum[-1])
    for i in range(1, n):
        for j in range(n-i):
            dp[j][j+i] = sys.maxsize
            for k in range(i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][j+k] + dp[j+k+1][j+i] + sum[j+i+1] - sum[j])
    answer.append(dp[0][n-1])
print(*answer,sep='\n')
