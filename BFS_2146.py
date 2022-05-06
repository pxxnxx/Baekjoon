import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
island = deque([])
mark = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0:
            queue = deque([[i,j]])
            visit[i][j] = 1
            arr[i][j] = mark
            island.append([i,j])
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    yy = y + dy[k]
                    xx = x + dx[k]
                    if 0 <= yy < n and 0 <= xx < n and visit[yy][xx] == 0 and arr[yy][xx] > 0:
                        queue.append([yy,xx])
                        visit[yy][xx] = 1
                        arr[yy][xx] = mark
            mark += 1
mark = 1
answer = sys.maxsize
for a, b in island:
    queue = deque([[a,b]])
    visit = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    visit[a][b] = 1
    check = sys.maxsize
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < n:
                if arr[yy][xx] == 0:
                    if visit[yy][xx] > visit[y][x] + 1:
                        visit[yy][xx] = visit[y][x] + 1
                        queue.append([yy,xx])
                elif arr[yy][xx] == mark:
                    if visit[yy][xx] > visit[y][x]:
                        visit[yy][xx] = visit[y][x]
                        queue.append([yy,xx])
                else:
                    if visit[yy][xx] > visit[y][x] + 1:
                        visit[yy][xx] = visit[y][x] + 1
                        check = min(check, visit[yy][xx])


    answer = min(answer, check-2)
    mark += 1

print(answer)