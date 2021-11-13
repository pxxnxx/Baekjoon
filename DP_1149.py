import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(n):
    arr.append(list(map(int,input().split())))
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + arr[i][0]
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + arr[i][1]
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + arr[i][2]
print(min(dp[i+1][0],dp[i+1][1],dp[i+1][2]))
