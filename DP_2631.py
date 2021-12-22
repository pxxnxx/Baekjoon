import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [1 for _ in range(n)]
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(n-max(dp))
