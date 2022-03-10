import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

answer = 0
def DFS(y, x, s, v):
    global answer
    if v == 4:
        answer = max(answer, s)
        return
    visit[y][x] = 1
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < m and visit[yy][xx] == 0:
            DFS(yy, xx, s+arr[yy][xx], v+1)
    visit[y][x] = 0
def T(y, x):
    global answer
    for k in range(4):
        s = arr[y][x]
        b = 1
        for i in range(4):
            if i == k:
                continue
            yy = y + dy[i]
            xx = x + dx[i]
            if yy < 0 or xx < 0 or yy >= n or xx >= m:
                b = 0
                break
            s += arr[yy][xx]
        if b:
            answer = max(answer, s)
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for i in range(n):
    for j in range(m):
        DFS(i, j, 0, 0)
        T(i, j)
print(answer)
