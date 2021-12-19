import sys
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
arr = list(map(int,input().split()))
m = int(input())

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for i in range(2,n+1):
    for s in range(n-i):
        e = s + i
        if arr[s] == arr[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1

answer = []
for i in range(m):
    s, e = map(int,input().split())
    answer.append(dp[s-1][e-1])
for x in answer:
    print(x)

