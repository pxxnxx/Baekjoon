from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]
deg = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    deg[b] += 1
queue = []
answer = []
for i in range(1, n+1):
    if deg[i] == 0:
        heappush(queue, i)

while queue:
    index = heappop(queue)
    answer.append(index)
    for x in arr[index]:
        deg[x] -= 1
        if deg[x] == 0:
            heappush(queue, x)
print(*answer, sep=' ')