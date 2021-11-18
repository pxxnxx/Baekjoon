import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
dp = [0 for _ in range(m+1)]
dp[0] = 1
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(1, m+1):
        if j - arr[i] >= 0:
            dp[j] += dp[j-arr[i]]
print(dp[m])
