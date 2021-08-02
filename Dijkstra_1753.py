import sys
from heapq import heappush, heappop
input = sys.stdin.readline
v, e = map(int,input().split())
start = int(input())
arr = [[] for _ in range(v+1)]
dist = [sys.maxsize] * (v+1)
dist[start] = 0
for i in range(e):
    a, b, c = map(int,input().split())
    arr[a].append((b,c))

def dijkstra(start):
    heap = []
    heappush(heap,(0, start))
    while heap:
        weight, index = heappop(heap)
        if dist[index] < weight:
            continue
        for x, y in arr[index]:
            if weight + y < dist[x]:
                dist[x] = weight + y
                heappush(heap,(dist[x],x))
dijkstra(start)
for i in range(1,len(dist)):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])
            
    
