import sys
input = sys.stdin.readline

def mirror(y,x,v):
    while 0 <= y < n and 0 <= x < m:
        if arr[y][x] == 1:
            if v%2 == 0:
                v = (v+1)%4
            else:
                v = (v-1)%4
        y += dy[v]
        x += dx[v]
    answer.append([y, x])


n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
num = [[0 for _ in range(m+2)] for _ in range(n+2)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
answer = []
k = 1

for i in range(n):
    num[i+1][0] = k
    mirror(i,0,0)
    k += 1
for i in range(m):
    num[n+1][i+1] = k
    mirror(n-1,i,1)
    k += 1
for i in range(n-1,-1,-1):
    num[i+1][m+1] = k
    mirror(i,m-1,2)
    k += 1
for i in range(m-1,-1,-1):
    num[0][i+1] = k
    mirror(0,i,3)
    k += 1
for y, x in answer:
    y += 1
    x += 1
    print(num[y][x], end=' ')