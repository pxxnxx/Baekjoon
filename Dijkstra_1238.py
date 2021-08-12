import sys
from heapq import heappop, heappush

def dijkstra(start):
    heap = []
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    heappush(heap,(start,0))
    while heap:
        ind, deg = heappop(heap)
        if dist[ind] < deg:
            continue
        for ne, we in arr[ind]:
            if dist[ne] > deg + we:
                dist[ne] = deg + we
                heappush(heap,(ne,dist[ne]))
    if start != x:
        return dist[x]
    else:
        return dist
        

n, m, x = map(int,input().split())
arr = [[] for _ in range(n+1)]
answer = [0] * (n+1)
for i in range(m):
    s, e, d = map(int,input().split())
    arr[s].append((e,d))

for i in range(1,n+1):
    if i != x:
        answer[i] = dijkstra(i)
    else:
        key = dijkstra(i)
for i in range(1,n+1):
    answer[i] += key[i]
print(max(answer))
