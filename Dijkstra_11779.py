import sys
from heapq import heappop, heappush
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
prev = [-1 for _ in range(n+1)]
for i in range(m):
    s, e, v = map(int,input().split())
    arr[s].append([e,v])
start, end = map(int,input().split())

def dijkstra(first):
    heap = []
    dist[first] = 0
    heappush(heap,(first, dist[first]))
    while heap:
        index, weight = heappop(heap)
        if dist[index] < weight:
            continue
        for x, y in arr[index]:
            if dist[x] > weight + y:
                dist[x] = weight + y
                prev[x] = index
                heappush(heap, (x, dist[x]))
dijkstra(start)
a = end
answer = []
while a != -1:
    answer.append(a)
    a = prev[a]
print(dist[end])
print(len(answer))
for i in range(len(answer)-1, -1, -1):
    print(answer[i],end=' ')
print()