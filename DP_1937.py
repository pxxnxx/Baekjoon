import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n = int(input())
arr = []
dp = [[1 for _ in range(n)] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
for i in range(n):
    arr.append(list(map(int,input().split())))

def dps(y,x):
    if dp[y][x] != 1:
        return dp[y][x]
    if visit[y][x] == 1:
        return 1
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < n and arr[yy][xx] > arr[y][x]:
            a = dps(yy, xx)
            if dp[y][x] < a + 1:
                dp[y][x] = a + 1
    visit[y][x] = 1
    return dp[y][x]
for i in range(n):
    for j in range(n):
        if dp[i][j] == 1:
            dps(i, j)
answer = 0
for i in range(n):
    if answer < max(dp[i]):
        answer = max(dp[i])
print(answer)

