import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int,input().split())
arr = [list(map(int,(str(input().strip())))) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
vvisit = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([[0, 0]])
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
while queue:
    y, x = queue.popleft()
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < n and 0 <= xx < m:
            if vvisit[yy][xx] == 0:
                if arr[yy][xx] == 0:
                    visit[yy][xx] = visit[y][x]
                else:
                    visit[yy][xx] = visit[y][x] + 1
                queue.append([yy, xx])
                vvisit[yy][xx] = 1
            else:
                if arr[yy][xx] == 0:
                    if visit[yy][xx] > visit[y][x]:
                        visit[yy][xx] = visit[y][x]
                        queue.append([yy, xx])
                else:
                    if visit[yy][xx] > visit[y][x] + 1:
                        visit[yy][xx] = visit[y][x] + 1
                        queue.append([yy, xx])
print(visit[n-1][m-1])

