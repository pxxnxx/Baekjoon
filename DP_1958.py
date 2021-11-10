import sys
input = sys.stdin.readline
arr = [0,0,0]
for i in range(3):
    arr[i] = input().strip()
a = len(arr[0])
b = len(arr[1])
c = len(arr[2])
dp = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]

for i in range(a):
    for j in range(b):
        for k in range(c):
            if arr[0][i] == arr[1][j] == arr[2][k]:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1],dp[i+1][j][k+1],dp[i+1][j+1][k],dp[i][j][k]+1)
            else:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1],dp[i+1][j][k+1],dp[i+1][j+1][k],dp[i][j][k])
                
print(dp[i+1][j+1][k+1])
