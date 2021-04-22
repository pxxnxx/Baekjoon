import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
heap = []
arr = [[] for _ in range(1001)]
m = 0
for _ in range(n):
    a, b = map(int,input().split())
    arr[a].append(b)
    if m < a:
        m = a

answer = 0
for i in range(m, 0, -1):
    for x in arr[i]:
        heappush(heap, [-x, x])
    if heap:
        answer += heappop(heap)[1]
print(answer)