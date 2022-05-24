import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
queue = deque([[0,0]])
visit[0][0] = 1
while queue:
    y, x = queue.popleft()
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < m and arr[yy][xx] == 1 and visit[yy][xx] == 0:
            visit[yy][xx] = visit[y][x] + 1
            queue.append([yy,xx])
print(visit[n-1][m-1])





