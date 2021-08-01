import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)
for i in range(m):
    a, b, c = map(int,input().split())
    arr[a].append((b,c))
first, last = map(int,(input()).split())

def dijkstra(first):
    heap = []
    heappush(heap, (0,first))
    dist[first] = 0
    while heap:
        weight, index = heappop(heap)
        if dist[index] < weight: 
            continue 
        for x, y in arr[index]:
            if dist[x] > weight + y:
                dist[x] = weight + y
                heappush(heap,(dist[x],x))
dijkstra(first)
print(dist[last])
