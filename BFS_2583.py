import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

m, n, k = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
dy = [0,-1,0,1]
dx = [1,0,-1,0]
for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
queue = deque([])
answer = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            queue.append([i, j])
            arr[i][j] = 1
            s = 0
            while queue:
                y, x = queue.popleft()
                s += 1
                for k in range(4):
                    yy = y + dy[k]
                    xx = x + dx[k]
                    if 0 <= yy < m and 0 <= xx < n and arr[yy][xx] == 0:
                        queue.append([yy, xx])
                        arr[yy][xx] = 1
            answer.append(s)
print(len(answer))
print(*sorted(answer),sep=' ')