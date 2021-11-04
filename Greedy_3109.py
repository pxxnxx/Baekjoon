import sys
input = sys.stdin.readline

def dfs(y, x):
    global answer
    arr[y][x] = 'x'
    if x == m-1:
        answer += 1
        return 1

    if 0 <= y-1 and arr[y-1][x+1] != 'x':
        if dfs(y-1, x+1):
            return 1
    if arr[y][x+1] != 'x':
        if dfs(y, x+1):
            return 1
    if y+1 < n and arr[y+1][x+1] != 'x':
        if dfs(y+1, x+1):
            return 1
    return 0

n, m = map(int,input().split())
arr = [list(str(input().strip())) for _ in range(n)]
answer = 0
for i in range(n):
    dfs(i, 0)
print(answer)