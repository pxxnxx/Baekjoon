import sys
input = sys.stdin.readline

arr = input().strip()
brr = input().strip()

dp = [[0 for _ in range(len(brr)+1)] for _ in range(len(arr)+1)]
str = [['' for _ in range(len(brr)+1)] for _ in range(len(arr)+1)]

for i in range(1,len(arr)+1):
    for j in range(1,len(brr)+1):
        if arr[i-1] == brr[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            str[i][j] = str[i-1][j-1] + arr[i-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if dp[i-1][j] < dp[i][j-1]:
                str[i][j] = str[i][j-1]
            else:
                str[i][j] = str[i-1][j]

print(dp[i][j])
if dp[i][j] != 0:
    print(str[i][j])
            
