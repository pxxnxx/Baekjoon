import sys
input = sys.stdin.readline

def dfs(x,y,z):
    global answer
    answer = max(answer,z)

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < r and 0 <= yy < c and key[arr[xx][yy]] == 0:
            key[arr[xx][yy]] = 1
            dfs(xx,yy,z+1)
            key[arr[xx][yy]] = 0
            
r, c = map(int,input().split())
arr = [list(map(lambda x : ord(x)-65, input().strip())) for _ in range(r)]
key = [0] * 26
answer = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
key[arr[0][0]] = 1
dfs(0,0,answer)
print(answer)
