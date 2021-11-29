import sys
input = sys.stdin.readline
n = int(input())
arr = []
m = 1000000

for i in range(n):
    arr.append(list(map(int,input().split())))
for f in range(3):
    dp = [[1000000 for _ in range(3)] for _ in range(n)]
    dp[0][f] = arr[0][f]
    for i in range(n-2):
        dp[i+1][0] = min(dp[i][1], dp[i][2]) + arr[i+1][0]
        dp[i+1][1] = min(dp[i][0], dp[i][2]) + arr[i+1][1]
        dp[i+1][2] = min(dp[i][0], dp[i][1]) + arr[i+1][2]
    dp[n-1][(f+1)%3] = min(dp[n-2][f%3], dp[n-2][(f+2)%3]) + arr[n-1][(f+1)%3]
    dp[n-1][(f+2)%3] = min(dp[n-2][f%3], dp[n-2][(f+1)%3]) + arr[n-1][(f+2)%3]
    if m > min(dp[n-1]):
        m = min(dp[n-1])
print(m)
