import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m = map(int,input().split())
dist = [sys.maxsize] * (n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, v = map(int,input().split())
    arr[s].append([e,v])
    arr[e].append([s,v])

heap = [[0,1]]
while heap:
    weight, start = heappop(heap)
    if dist[start] < weight:
        continue
    for index, value in arr[start]:
        if dist[index] > value + weight:
            dist[index] = value + weight
            heappush(heap, [dist[index], index])
print(dist[n])