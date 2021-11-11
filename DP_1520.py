import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
dp = [[-1 for _ in range(m)] for _ in range(n)]
dy = [0,0,-1,1]
dx = [1,-1,0,0]

for i in range(n):
    arr.append(list(map(int,input().split())))
def DFS(y,x):
    if y == n-1 and x == m-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0

    for i in range(4):  
        yy = y + dy[i]
        xx = x + dx[i]
        if yy >= 0 and xx >= 0 and yy < n and xx < m and arr[y][x] > arr[yy][xx]:
            dp[y][x] += DFS(yy,xx)
    return dp[y][x]

print(DFS(0,0))
