import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
visit = [[0 for _ in range(m)] for _ in range(n)]
queue = []
check = 0
year = 0
dy = [0,0,-1,1]
dx = [1,-1,0,0]
for i in range(n):
    arr.append(list(map(int,input().split())))

while True:
    # Check
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0 and arr[i][j] > 0:
                queue.append([i,j])
                visit[i][j] = 1
                check += 1
                
                while queue:
                    y = queue[0][0]
                    x = queue[0][1]
                    del queue[0]
                    for k in range(4):
                        yy = y + dy[k]
                        xx = x + dx[k]
                        if 0 <= yy and n > yy and 0 <= xx and m > xx and visit[yy][xx] == 0 and arr[yy][xx] > 0:
                            queue.append([yy,xx])
                            visit[yy][xx] = 1
                            
    if 2 <= check:
        print(year)
        break
    
    max = 0
    for i in range(n):
        for j in range(m):
            if max < arr[i][j]:
                max = arr[i][j]
    if 0 == max:
        print(0)
        break


    check = 0
    for i in range(n):
        for j in range(m):
            visit[i][j] = 0
    # Decrease
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                visit[i][j] = 1
                for k in range(4):
                    yy = i + dy[k]
                    xx = j + dx[k]
                    if 0 <= yy and n > yy and 0 <= xx and m > xx and visit[yy][xx] == 0 and arr[yy][xx] <= 0:
                        arr[i][j] -= 1
    year += 1
    for i in range(n):
        for j in range(m):
            visit[i][j] = 0
    
                    
           






