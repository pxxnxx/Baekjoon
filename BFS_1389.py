import sys
from collections import deque
n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

def BFS(k):
    queue = deque([k])
    level = [0] * n
    check = [False] * n
    check[k] = True
    while queue:
        x = queue.popleft()
        for key in arr[x]:
            if not check[key]:
                queue.append(key)
                level[key] = level[x] + 1
                check[key] = True
    return sum(level)

answer = []
for i in range(n):
    answer.append(BFS(i))
        
print(answer.index(min(answer))+1)
