import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [[] for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
for i in range(m):
    start, end, val = map(int,input().split())
    arr[start].append([end, val])
    arr[end].append([start, val])

ms, me = map(int,input().split())
def dijkstra(first):
    heap = []
    heappush(heap, (first, 0))
    dist[first] = 0
    while heap:
        index, weight = heappop(heap)
        if dist[index] < weight:
            continue
        for x, y in arr[index]:
            if dist[x] > weight + y:
                dist[x] = weight + y
                heappush(heap,(x, dist[x]))
dijkstra(1)
answera = dist[ms]
answerb = dist[me]
dist = [sys.maxsize for _ in range(n+1)]
dijkstra(ms)
answera += dist[me]
b = dist[n]
dist = [sys.maxsize for _ in range(n+1)]
dijkstra(me)
answerb += dist[ms]
a = dist[n]
answer = min(answera+a, answerb+b)
if answer >= sys.maxsize:
    print(-1)
else:
    print(answer)