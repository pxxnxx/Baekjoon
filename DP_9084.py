import sys
input = sys.stdin.readline
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for i in range(len(arr)):
        for j in range(1,m+1):
            if j-arr[i] >= 0:
                dp[j] += dp[j-arr[i]]
    answer.append(dp[m])
for x in answer:
    print(x)