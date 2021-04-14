import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)
heap = []
for i in range(m):
    start, end, weight = map(int,input().split())
    arr[start].append([end, weight])
    arr[end].append([start, weight])

s, t = map(int,input().split())

dist[s] = 0
heappush(heap,[s, 0])
while heap:
    now, weight = heappop(heap)
    if dist[now] < weight:
        continue
    for y, x in arr[now]:
        if dist[y] < weight + x:
            continue
        dist[y] = weight + x
        heappush(heap, [y, weight + x])
print(dist[t])
