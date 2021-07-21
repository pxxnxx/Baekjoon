def BFS(x,y,z):
    queue = []
    queue.append([x,y])
    cnt = 1
    arr[x][y] = 0
    while queue:
        for i in range(4):
            xx = queue[0][0] + dx[i]
            yy = queue[0][1] + dy[i]
            if xx >= 0 and yy >= 0 and xx < m and yy < n:
                if arr[xx][yy] == z:
                    queue.append([xx,yy])
                    arr[xx][yy] = 0
                    cnt += 1
        del queue[0]
    return cnt * cnt
n,m = map(int,input().split())
brr = []
arr = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(m):
    brr.append(input())
B = 0
W = 0
for i in range(m):
    for j in range(n):
        if brr[i][j] == 'W':
            arr[i][j] = 1
        elif brr[i][j] == 'B':
            arr[i][j] = 2

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:       
            W += BFS(i,j,1)
for i in range(m):
    for j in range(n):
        if arr[i][j] == 2:
            B += BFS(i,j,2)
print(W,B)
