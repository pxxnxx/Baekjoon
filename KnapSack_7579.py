import sys
input = sys.stdin.readline

#  TODO
#   복습 할 것

n, m = map(int,input().split())
value = list(map(int,input().split()))
weight = list(map(int,input().split()))
sw = sum(weight)
sv = sum(value)
dp = [0 for _ in range(sw+1)]
for i in range(n):
    for j in range(sw, weight[i]-1, -1):
        dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
for i in range(sw+1):
    if dp[i] >= m:
        print(i)
        break