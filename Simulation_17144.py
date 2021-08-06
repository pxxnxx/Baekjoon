import sys
import copy
input = sys.stdin.readline
r,c,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    if arr[i][0] == -1:
        air = i
        break
n = copy.deepcopy(arr)
for _ in range(t):
    arr = copy.deepcopy(n) # deepcopy 아니면 연결됨 
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                queue=[]
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    if x>=0 and x<c and y>=0 and y<r and arr[y][x] != -1:
                        queue.append((y,x))
                for yy, xx in queue:
                    n[yy][xx] += arr[i][j] // 5
                    n[i][j] -= arr[i][j] // 5

    for i in range(air-1,0,-1):
        n[i][0] = n[i-1][0]
    for i in range(c-1):
        n[0][i] = n[0][i+1]
    for i in range(air):
        n[i][c-1] = n[i+1][c-1]
    for i in range(c-1,1,-1):
        n[air][i] = n[air][i-1]
    for j in range(air+2,r-1):
        n[j][0] = n[j+1][0]
    for j in range(c-1):
        n[r-1][j] = n[r-1][j+1]
    for j in range(r-1,air+1,-1):
        n[j][c-1] = n[j-1][c-1]
    for j in range(c-1,1,-1):
        n[air+1][j] = n[air+1][j-1]
    n[air][1] = 0
    n[air+1][1] = 0

answer = 2
for i in range(r):
    for j in range(c):
        answer += n[i][j]
print(answer)

