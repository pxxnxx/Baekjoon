import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int,input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for i in range(m):
    s, e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)
queue = deque([start])
visit[start] = 1
while queue:
    x = queue.popleft()
    if x == end:
        break
    for y in arr[x]:
        if visit[y] == 0:
            visit[y] = visit[x] + 1
            queue.append(y)
if visit[end] == 0:
    print(-1)
else:
    print(visit[end] - 1)