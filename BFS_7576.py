import sys
from collections import deque
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= 0 and yy >= 0 and xx < n and yy < m:
                
                if arr[xx][yy] == 0:
                    arr[xx][yy] = arr[x][y] + 1
                    queue.append([xx,yy])
                                   
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = []
queue = deque(queue)
m, n = map(int,sys.stdin.readline().split())
arr = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i,j])
            
BFS()
ma = 0
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer = -1
        if arr[i][j] > ma:
            ma = arr[i][j]
if answer == -1:
    print(-1)
else:
    print(ma-1)
