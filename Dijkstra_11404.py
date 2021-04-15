def dijkstra(start):
    heap = []
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    heappush(heap,(start,0))
    while heap:
        ind, deg = heappop(heap)
        # if dist[ind] > deg: 로 해도 맞음
        if dist[ind] < deg:
            continue
        for ne, we in arr[ind]:
            if dist[ne] > we + deg:
                dist[ne] = we + deg
                heappush(heap,(ne,dist[ne]))
    for i in range(n):
        if dist[i+1] != sys.maxsize:
            print(dist[i+1],end=' ')
        else:
            print("0",end=' ')
    print()

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int,input().split())
    arr[start].append((end,cost))
for i in range(n):
    dijkstra(i+1)

#98% 오류, 0일때 해결
