import sys
input = sys.stdin.readline
arr = input().strip()
brr = input().strip()
m = 0
dp = [[0 for _ in range(len(brr)+1)]]
for i in range(len(arr)):
    dp.append([0 for _ in range(len(brr) + 1)])
    for j in range(len(brr)):
        if arr[i] == brr[j]:
            dp[1][j+1] = dp[0][j] + 1
        else:
            dp[1][j+1] = 0
        if dp[1][j+1] > m:
            m = dp[1][j+1]
    del dp[0]
print(m)

