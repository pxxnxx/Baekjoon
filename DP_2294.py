import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr = []
dp = [10001 for _ in range(k+1)]
dp[0] = 0
for i in range(n):
    arr.append(int(input()))
arr = list(set(arr))
for i in range(len(arr)):
    for j in range(1, k+1):
        if j - arr[i] >= 0 and dp[j] > dp[j-arr[i]] + 1:
            dp[j] = dp[j-arr[i]] + 1
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

