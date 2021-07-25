import sys
from collections import deque
def BFS():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            xx = x + dx[i]
            yy = y + dy[i]
            zz = z + dz[i]
            if xx >= 0 and yy >= 0 and zz >=0 and xx < h and yy < n and zz < m:
                if arr[xx][yy][zz] == 0:
                    arr[xx][yy][zz] = arr[x][y][z] + 1
                    queue.append([xx,yy,zz])

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int,sys.stdin.readline().split()) # 
arr = [[[int(x) for x in sys.stdin.readline().split()] for y in range(n)] for z in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append([i,j,k])
day = 0
ma = 0
BFS()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                day = -1
            if arr[i][j][k] > ma:
                ma = arr[i][j][k]
if day == -1:
    print(-1)
else:
    print(ma-1)
