import sys
from heapq import heappop, heappush
sys.stdin = open("1781in.txt")
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
m = 0
for _ in range(n):
    a, b = map(int,input().split())
    arr[a].append(b)
    m = max(m, a)

heap = []
answer = 0
for i in range(m, 0, -1):
    for x in arr[i]:
        heappush(heap, -x)
    if heap:
        answer -= heappop(heap)
print(answer)