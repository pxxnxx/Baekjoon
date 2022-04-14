import sys
sys.setrecursionlimit(10**8)
def dfs(y, x):
    mp[y][x] = 2
    for i in range(4):
        yy = y+dy[i]
        xx = x+dx[i]
        if 0 <= yy < 2001 and 0 <= xx < 2001 and mp[yy][xx] == 1:
            dfs(yy,xx)

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for v in arr:
    for i in range(4):
        v[i] = (v[i]+500) * 2
mp = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(n):
    mp[arr[i][1]][arr[i][0]] = 1
    mp[arr[i][1]][arr[i][2]] = 1
    mp[arr[i][3]][arr[i][0]] = 1
    mp[arr[i][3]][arr[i][2]] = 1

    for j in range(arr[i][0]+1, arr[i][2]):
        mp[arr[i][1]][j] = 1
        mp[arr[i][3]][j] = 1
    for j in range(arr[i][1]+1, arr[i][3]):
        mp[j][arr[i][0]] = 1
        mp[j][arr[i][2]] = 1
answer = 0

for i in range(2001):
    for j in range(2001):
        if mp[i][j] == 1:
            answer += 1
            dfs(i, j)
if mp[1000][1000] == 2:
    answer -= 1

print(answer)