import sys
input = sys.stdin.readline

n = int(input())
arr = [[]]*n
visit = [[0 for _ in range(n)] for _ in range(n)]
dy = [-1,0,0,1]
dx = [0,-1,1,0]
queue = []
start = [0,0]
level = [2,2]
answer = 0
p = 10000
for i in range(n):
    arr[i] = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start[0] = i
            start[1] = j
            arr[i][j] = 0
            break 
queue.append([start[0],start[1]])

fy = -1
fx = -1
while queue:
    y = queue[0][0]
    x = queue[0][1]
    del queue[0]

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        
        if xx >= 0 and xx < n and yy >= 0 and yy < n and visit[yy][xx] == 0 and visit[y][x] < p:
            
            if arr[yy][xx] == level[0] or arr[yy][xx] == 0:
                visit[yy][xx] = visit[y][x] + 1
                queue.append([yy,xx])
                
            elif arr[yy][xx] < level[0]:
                queue.append([yy,xx])
                visit[yy][xx] = visit[y][x] + 1
                p = visit[yy][xx]
                
                if fy != -1:
                    if yy < fy:
                        fy = yy
                        fx = xx
                    elif yy == fy and xx < fx:
                        fy = yy
                        fx = xx
                else:
                    fy = yy
                    fx = xx

    if not queue: 
        if fy != -1:
            arr[fy][fx] = 0
            level[1] -= 1
            if level[1] == 0:
                level[0] += 1
                level[1] = level[0]
            queue.append([fy,fx])

            answer += p
            p = 10000
            fy = -1
            fx = -1
            for i in range(n):
                for j in range(n):
                    visit[i][j] = 0

print(answer)                      
                    
                                

