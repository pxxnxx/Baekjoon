from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]
deg = [0 for _ in range(n+1)]
for _ in range(m):
    inp = list(map(int,input().split()))
    for i in range(1, len(inp)-1):
        arr[inp[i]].append(inp[i+1])
        deg[inp[i+1]] += 1
queue = deque()
answer = []
for i in range(1, n+1):
    if deg[i] == 0:
        queue.append(i)

while queue:
    index = queue.popleft()
    answer.append(index)
    for x in arr[index]:
        deg[x] -= 1
        if deg[x] == 0:
            queue.append(x)
if len(answer) == n:
    print(*answer,sep='\n')
else:
    print(0)