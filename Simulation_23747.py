import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(str(input().strip())) for _ in range(n)]
y, x = map(int,input().split())
route = str(input().strip())
dy = [-1,0,0,1]
dx = [0,-1,1,0]
y -= 1
x -= 1
com = {"U":0, "L":1, "R":2, "D":3, "W":4}
for i in range(len(route)):
    if com[route[i]] < 4:
        y += dy[com[route[i]]]
        x += dx[com[route[i]]]
    else:
        queue = deque([[y, x]])
        check = arr[y][x]
        arr[y][x] = '.'
        if check != '.':
            while queue:
                now_y, now_x = queue.popleft()
                for j in range(4):
                    yy = now_y + dy[j]
                    xx = now_x + dx[j]
                    if 0 <= yy < n and 0 <= xx < m and arr[yy][xx] == check:
                        queue.append([yy,xx])
                        arr[yy][xx] = '.'
for i in range(4):
    yy = y + dy[i]
    xx = x + dx[i]
    if 0 <= yy < n and 0 <= xx < m:
        arr[yy][xx] = '.'
arr[y][x] = '.'
for i in range(n):
    for j in range(m):
        if arr[i][j] != '.':
            print("#",end='')
            continue
        print('.',end='')
    print()